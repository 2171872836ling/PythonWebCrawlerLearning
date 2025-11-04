"""
简化请求、响应、源代码
requests:第三方库->pip install requests
常用.*?，匹配度精确，但是正则表达式难写、运行运行效率低
"""
from tokenize import String

import requests
"=============================================================代理：防止被封IP==========================================================="
import random
def fetch_with_proxy(url):
    """
    使用代理服务器获取指定 URL 的内容
    :param url: 目标 URL
    :return: 请求的响应内容，如果失败返回 None
    """
    # 代理池
    proxy_pool = [
        "http://proxy1.example.com:8080",
        "http://proxy2.example.com:8080",
        "socks5://proxy3.example.com:1080",
        "socks5://proxy4.example.com:1080"
    ]

    # 随机打乱代理池顺序
    random.shuffle(proxy_pool)

    for proxy in proxy_pool:
        proxies = {
            "http": proxy,
            "https": proxy
        }
        try:
            response = requests.get(url, proxies=proxies, timeout=5)
            if response.status_code == 200:
                print(f"使用代理 {proxy} 成功获取内容")
                response.close()
                return response
            else:
                print(f"代理 {proxy} 无效，状态码: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"代理 {proxy} 无效，错误信息: {e}")
    print("所有代理均无效")
    return None



"=============================================================GET方法==========================================================="
def get_server_rendering():
    query=input("请输入你要搜索的对象：")
    #中文转码可能会出问题
    url=f"https://sogou.com/web?{query}"
    #设备验证：抓包获取user-agent信息->模拟一台设备，一般网站会要求获取设备信息，获取不到就会反爬
    User_Agent = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0"
    }
    response = requests.get(url,headers=User_Agent)
    print("response:",response)#响应状态，代码200正常访问
    print("response.text:",response.text)#get方法会出现验证，要User_Agent（反爬）
    response.close()


def get_client_rendering():
    """
    客户端渲染：数据和网页分离，数据一般在抓包的XHR
    :return:
    """
    #https://movie.douban.com/j/chart/top_list?type=25&interval_id=100%3A90&action=&start=0&limit=20
    #params：重新赋值参数->在？后面的参数
    url="https://movie.douban.com/j/chart/top_list"
    for i in range(0,60,20):#一页start就是20，这里示范3页
        #XHR的负载可以查看
        param={
            "type": 25,
            "interval_id": "100:90",
            "action": "",
            "start": i,
            "limit": 50
        }

        #get请求
        # response = requests.get(url,params=param)
        # print("response:",response)#输出结果是无：被反爬了->headers=User_Agent、cookic有问题
        #加个headers
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0"
        }
        response = requests.get(url, headers=headers, params=param)
        print(response.json())
        response.close()


"================================================================POST方法================================================================="
def post():
    s=input("请输入你要搜索的对象：")
    #POST访问方式的网址
    url=f"https://fanyi.baidu.com/sug"

    #负载或者From Data
    data = {
        "kw":s
    }

    #Post访问
    response = requests.post(url,data=data)
    #将响应信息转换为Josn
    print("response.json:",response.json())
    response.close()

if __name__ == '__main__':
    get_client_rendering()
    # get_server_rendering()
    # post()
    # fetch_with_proxy("http://fanyi.baidu.com")
    pass