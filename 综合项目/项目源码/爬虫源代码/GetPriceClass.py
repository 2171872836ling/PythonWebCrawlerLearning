import requests
import json
import pandas as pd
import os
import csv
import random
from datetime import datetime
from bs4 import BeautifulSoup

# openpyxl：隐藏的包形成xlsx表格的包

"""
# ==================第五组====================== #
（1）组员：
    潘炜麟
    罗子琪
    刘建斌

（2）声明：
    客户端渲染网页-爬取表头的网站(bs4)：f"http://www.xinfadi.com.cn/priceDetail.html"
    服务器渲染网页-爬取数据的网站(josn)：http://www.xinfadi.com.cn/priceDetail.html"
    爬虫访问次数频繁就是ddos攻击了，未经允许，切勿盲目爬取数据
"""


class CrawlDatas:
    # ======================================构造方法====================================== #
    def __init__(self):
        """
        初始化输出信息：
        """
        print("""
    # ============================================第五组================================================ #
    （1）组员：
        潘炜麟
        罗子琪
        刘建斌

    （2）声明：
        1.客户端渲染网页-爬取表头的网站(bs4)：f"http://www.xinfadi.com.cn/priceDetail.html"
        2.服务器渲染网页-爬取数据的网站(josn)：http://www.xinfadi.com.cn/priceDetail.html"
        3.爬虫访问次数频繁就是ddos攻击了，未经允许，切勿盲目爬取数据
        4.经测试爬取100万条以上才使用代理池，但网页有崩溃的风险（警惕使用）
    """)


    # =============================================================================反爬机制(一般用不到)============================================================================= #
        #1.header表头，cookic验证
    __headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    }
    __cookic={
        "buvid3=C8CAD503-8F66-4BDC-DD2D-9889BAB7448518849infoc; b_nut=1747194618; _uuid=C10EE282D-2B35-FBFE-C78B-642DE105EB5E919757infoc; buv"
        "id_fp=2b49f1b32db35c02f32e95f17240071b; header_theme_version=CLOSE; enable_web_push=DISABLE; enable_feed_channel=ENABLE; buvid4=41FADC"
        "55-2EE1-599E-3539-3C484187AD7C20712-025051411-ZYzo6oVOMYciI5cxckI5cQhWKX5C9RyPz0nFMG6E%2FCVOUPsIGP2BCTE0fuLkf5q1; DedeUserID=695064167; "
        "DedeUserID__ckMd5=dfbe470657bb13c8; rpdid=0zbfVHhWcU|iCCWYPtO|2Jf|3w1Uf6Lf; LIVE_BUVID=AUTO6417484292526039; CURRENT_QUALITY=80; hit-dyn-v"
        "2=1; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTExMjQzMDUsImlhdCI6MTc1MDg2NTA0NSwicGx0IjotMX0.GAKisOmX0C"
        "vfnzP5R5TpmIgyyQoTzg8khM2ZvKZ_8zQ; bili_ticket_expires=1751124245; SESSDATA=64830338%2C1766417106%2Cd8501%2A62CjBhiA1v9hbXOIUBqFPNwKH_wg5sudI"
        "YnakPgh-jTPwEsph3hoP9ONr-6EnpyPmRy4ISVmRxSlFfbUZGdldHV2xCV081X1FOWDF1Yzk3d3l3cm9Yb2tpaktnc09VSzJDUUw2U1NyNXRaTFJOWEhOTzlueVhnbVF1MTF1X0E2bE"
        "9EWDJ5alF0eklBIIEC; bili_jct=b5d2381f07b8bc65fd22a05766e9e8f2; bp_t_offset_695064167=1082497376825901056; CURRENT_FNVAL=2000; b_lsid=9BADB89C"
        "_197AF4DF55F; home_feed_column=4; browser_resolution=447-753; sid=7a5exyf0"
    }
    #2.代理池（未使用，测试过爬取100万条以上才使用，但网页有崩溃的风险）
    # 请求头，模拟浏览器访问，避免被网站识别为爬虫


    def get_random_proxy(self,url):
        """
        爬取免费代理并验证，返回一个可用的代理。
        如果没有可用代理，则返回 None。
        """
        # 用于存储爬取到的代理的列表
        proxy_pool = []

        # 爬取代理的函数
        def crawl_proxies():
            """
            从指定的代理网站爬取代理 IP 和端口，并将它们添加到 proxy_pool 列表中。
            """
            # 代理网站的 URL

            try:
                # 发送 HTTP 请求
                response = requests.get(url, headers=headers)
                # 检查响应状态码
                if response.status_code == 200:
                    # 使用 BeautifulSoup 解析 HTML 内容
                    soup = BeautifulSoup(response.text, "html.parser")
                    # 找到包含代理信息的表格行
                    rows = soup.find_all("tr", class_="odd")
                    for row in rows:
                        # 提取每一行的单元格
                        tds = row.find_all("td")
                        if len(tds) > 1:
                            # 提取 IP 和端口
                            ip = tds[1].text
                            port = tds[2].text
                            # 构造代理字符串
                            proxy = f"{ip}:{port}"
                            # 将代理添加到代理池
                            proxy_pool.append(proxy)
                    print(f"成功爬取到 {len(proxy_pool)} 个代理")
                else:
                    print("爬取代理失败，状态码：", response.status_code)
            except Exception as e:
                print("爬取代理时发生错误：", e)

        # 验证代理是否可用的函数
        def validate_proxy(proxy):
            """
            验证代理是否可用，通过访问一个测试网站来检查代理是否能成功连接。
            如果代理可用，返回 True；否则返回 False。
            """
            # 测试代理的 URL
            test_url = "http://httpbin.org/ip"
            # 构造代理字典
            proxies = {
                "http": proxy,
                "https": proxy
            }
            try:
                # 发送 HTTP 请求，设置超时时间为 5 秒
                response = requests.get(test_url, proxies=proxies, timeout=5)
                # 检查响应状态码
                if response.status_code == 200:
                    print(f"代理 {proxy} 可用")
                    return True
                else:
                    print(f"代理 {proxy} 不可用")
                    return False
            except:
                print(f"代理 {proxy} 不可用")
                return False

        # 调用爬取代理的函数
        crawl_proxies()

        # 验证并筛选可用代理
        valid_proxies = [proxy for proxy in proxy_pool if validate_proxy(proxy)]

        # 如果有可用代理，随机返回一个
        if valid_proxies:
            return random.choice(valid_proxies)
        else:
            print("没有可用的代理")
            return None


    def get_price_datas(self, limit:int, prod_pcatid: int, get_table_head_url: str =f"http://www.xinfadi.com.cn/priceDetail.html",get_price_datas_url: str =f"http://www.xinfadi.com.cn/getPriceData.html"):
        """
        代码解析数据，网址基本固定
        :param url: 抓包获取服务器网页的网址
        :param limit:通过网页data中limit的分析获取规律，改变爬取的数量
        :param prod_pcatid:通过网页data中prodPcatid的分析获取规律，改变爬取方向（蔬菜1186，水果1187，粮油1188，肉禽蛋1189，水产1190，豆制品1203，调料1204）
        :return: 列表
        """
        # ==============================================================获取表头=======================================================================#
        response = requests.post(url=get_table_head_url)
        # print(response.text)

        # 2.把页面源代码传给BeautfulSoup处理，生成bs对象，如果features不传参默认html，但会警告
        page = BeautifulSoup(response.text, "html.parser")  # 指定html解析器,parser:解析器
        # print(page)

        # 3.从bs对象查询数据
        # find(标签，属性=值)     找第一个就返回
        # find all(标签，属性=值)     返回所有
        # (1)把table的提取出来
        # table = page.find("table",class_ ="hg table")# class是python的关键字,用class_处理
        tables = page.find("table", attrs={"border": "0", "cellpadding": "0", "cellspacing": "0"})  # 但也可以转化成字典，一般用这个
        # print(tables)
        # (2)再从table里面提取th（行）的标签
        trs = tables.find_all("th")
        # print(trs)
        # (3)再从trs里面提取"行"具体的数据,把数据放入HandAll
        table_head_prodCat = trs[0].text  # 一级分类
        table_head_prodPcat = trs[1].text  # 二级分类
        table_head_prodName = trs[2].text  # 品名
        table_head_lowPrice = trs[3].text  # 最低价
        table_head_AvgPrice = trs[4].text  # 平均价
        table_head_highPrice = trs[5].text  # 最高价
        table_head_specInfo = trs[6].text  # 规格
        table_head_place = trs[7].text  # 产地
        table_head_unitInfo = trs[8].text  # 单位
        table_head_pubDate = trs[9].text  # 发布日期
        # print(table_head_prodCat, table_head_prodPcat, table_head_prodName, table_head_lowPrice, table_head_AvgPrice, table_head_highPrice,
        #                 table_head_specInfo, table_head_place, table_head_unitInfo, table_head_pubDate)
        response.close()
        # ==============================================================获取价格数据=======================================================================#

        # 发送HTTP请求
        try:
            response = requests.post(url=get_price_datas_url, data={"limit": limit, "prodPcatid": prod_pcatid})
            response.raise_for_status()  # 检查请求是否成功
            response = json.loads(response.text)  # 获取原数据
            # 筛选数据
            listjson = list()
            for i in response["list"]:
                prodCat = i["prodCat"]
                prodPcat = i["prodPcat"]
                prodName = i["prodName"]
                lowPrice = i["lowPrice"]
                avgPrice = i["avgPrice"]
                highPrice = i["highPrice"]
                specInfo = i["specInfo"]
                place = ",".join(i["place"])  # 省份加空格分开
                unitInfo = i["unitInfo"]
                pubDate = i["pubDate"]
                listjson.append({table_head_prodCat: prodCat, table_head_prodPcat: prodPcat, table_head_prodName: prodName, table_head_lowPrice: lowPrice,
                                 table_head_AvgPrice: avgPrice, table_head_highPrice: highPrice, table_head_specInfo: specInfo, table_head_place: place,
                                 table_head_unitInfo: unitInfo, table_head_pubDate: pubDate})
            # print(listjson)
            return listjson
        except requests.RequestException as e:
            return f"请求错误: {e}"

    def print_datas(self, datas):
        """
        标准输出爬取的数据
        :param datas:爬取的列表
        :return: 无
        """
        # 输出数据
        try:
            for i in datas:
                print(
                    f"{i['一级分类']:<4}{('NaN' if not i['二级分类'] else str(i['二级分类'])):<10}{i['品名']:<10}{i['最低价']:<10}{i['平均价']:<10}{i['最高价']:<10}{i['规格']:<10}{i['产地']:<10}{i['单位']:<10}{i['发布日期']:<10}")
        except Exception as e:
            print("异常: ", e)

    def save_style(self, josn_datas, select_save_style: str) -> str:
        """
        保存爬取的数据: 命名通过文件名+时间,避免覆盖抓取的文件。
        保存格式: 这里我只弄了3种，可以加个word和txt。
        :param josn_datas:保存的数据
        :param select_save_style:保存的方式,输入数字，注意是字符串!!!input转int懒得写异常捕抓（1.xlsx 2.json 3.scv）
        :return:文件保存位置和时间
        """
        try:
            # ===================（1）获取时间====================== #
            current_time = datetime.now().strftime("-%Y-%m-%d-%H-%M-%S")  # 获取当前时间,格式化时间，精确到秒，用来区分文件->避免强制覆盖
            # =================（2）初始化输出文件夹=================== #
            # 保存位置
            path = "./数据保存位置/价格表" + current_time
            # 检查输出文件夹是否存在，如果不存在则创建
            os.makedirs(os.path.dirname(path), exist_ok=True)
            # ============（3）重构输出位置，定义文件名================ #
            if select_save_style == "0":
                return f"放弃保存，时间戳: {current_time}"

            elif select_save_style == "1":
                # (1)将数据保存为Excel表
                # 将数据转换为 DataFrame
                df = pd.DataFrame(josn_datas)
                # 保存到Excel文件
                df.to_excel(path + "价格表.xlsx", index=False, engine="openpyxl")
                return f"数据已成功保存到 {path + '.xlsx'}"

            elif select_save_style == "2":
                #  (2)将数据保存为josn,弄出来转义字符，可以通过ensure_ascii=False调整
                with open(path + "价格表.json", mode="w", encoding="utf-8") as file:
                    json.dump(josn_datas, file, indent=4)
                return f"数据已成功保存到 {path + '.json'}"

            elif select_save_style == "3":
                #  (3)将数据保存为scv
                with open(path + "价格表.csv", mode="w", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerows(josn_datas)
                return f"数据已成功保存到 {path + '.scv'}"
            else:
                return "保存选择方式输入错误！"
        # ===========异常处理================= #
        except Exception as e:
            return e



if __name__ == "__main__":
    # ======================测试======================== #
    # i = CrawlDatas()
    # datas = i.get_price_datas(2, 1186)
    # i.print_datas(datas)
    # datas = i.get_price_datas(2, 1187)
    # i.print_datas(datas)
    # datas = i.get_price_datas(2, 1188)
    # i.print_datas(datas)
    # datas = i.get_price_datas(2, 1189)
    # i.print_datas(datas)
    # datas = i.get_price_datas(2, 1190)
    # i.print_datas(datas)
    # datas = i.get_price_datas(2, 1203)
    # i.print_datas(datas)
    # datas = i.get_price_datas(2, 1204)
    # i.print_datas(datas)
    # print(i.save_style(datas, "1"))
    # print(i.save_style(datas, "2"))
    # print(i.save_style(datas, "3"))
    # 主函数（黑框框控制台输出）

    # ======================主函数======================== #
    CrawlDatas = CrawlDatas()
    while True:
        #获取数据
        prod_pcatid=input("""\n爬取类型有:\n0: 退出程序\n1: 蔬菜\n2: 水果\n3: 粮油\n4: 肉禽蛋\n5: 水产\n6: 豆制品\n7: 调料\n请输入爬取类型(输入0,1,2,3...7回车)：""").strip()
        if prod_pcatid == "0":
            exit()#退出程序
        elif prod_pcatid == "1":
            prod_pcatid="1186"
        elif prod_pcatid == "2":
            prod_pcatid="1187"
        elif prod_pcatid == "3":
            prod_pcatid="1188"
        elif prod_pcatid == "4":
            prod_pcatid="1189"
        elif prod_pcatid == "5":
            prod_pcatid="1190"
        elif prod_pcatid == "6":
            prod_pcatid="1203"
        elif prod_pcatid == "7":
            prod_pcatid="1204"
        else:
            print("输入错误！请重新输入！")
        limit=input("请输入爬取的数量（条）：").strip()
        datas=CrawlDatas.get_price_datas(limit, prod_pcatid)

        # 保存数据
        select=input("""\n保存格式有:\n0: 放弃保存\n1: Excel表\n2: json\n3: scv\n请输入保存格式(输入0,1,2,3回车)：""").strip()
        #自带判断
        print(CrawlDatas.save_style(josn_datas=datas, select_save_style=select))
        print("-------------------------------------爬取完毕---------------------------------------")



