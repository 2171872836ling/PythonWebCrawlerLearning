import csv
import json
import re

import requests
"""
A级加密网站
1.定位网页
2.获取网页源码(加密)：在get参数中启用verify=False->去掉安全认证，但会警告InsecureRequestWarning,否则会报SSlEroor
3.获取下载链接,加密过，生成的链接无法直接打开
声明：2025.11.3不启用verify=False也能爬到源代码
"""

domain =f"https://www.dytt89.com/"
response = requests.get(domain)#, verify=False)
#老规矩，爬出来编码错误，找charset的属性=网页编码
response.encoding = "gb2312"
# print(response.text)#测试
#开始爬数据,正则表达式定位
obj1 = re.compile(r'2025必看热片.*?<ul>(?P<ul>.*?)</ul>', re.S)#拿到ul里面li的数据
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)#获取子页面链接
obj3=re.compile(r'◎片　　名(?P<MovieName>.*?)<br />'
                r'.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<MovieDownloadHref>.*?)">',re.S)#子网页的电影名字,子网页的下载链接

#记录完整链接
movie_href=list()
#记录片名和下载链接
record_all=dict()


# 遍历电影名字
result=obj1.finditer(response.text)
for i in result:
    ul=i.group('ul').strip()
    # print(ul)#测试
    # 遍历电影子链接
    result=obj2.finditer(ul)
    for i in result:
        # 主链接+字链接=网站链接
        movie_href.append(domain + i.group('href').strip("/"))
        # print(i.group('href').strip())#测试
response.close()#主页面的访问状态关闭



#遍历访问子页面
for href in movie_href:
    child_response = requests.get(href)
    child_response.encoding = "gb2312"
    # print(child_response.text)#测试
    result3=obj3.search(child_response.text)
    print("电影名字:",result3.group('MovieName').strip())
    print("下载链接:",result3.group('MovieDownloadHref').strip())
    #转换为字典写入record_all
    record_all.update({result3.group('MovieName').strip(): result3.group('MovieDownloadHref').strip()})
    child_response.close()
    break

# with open("movie_record.txt","w",encoding="utf-8") as f:
#     csvwriter = csv.writer(f)
#     csvwriter.writerow(record_all.keys())
print(record_all)
























