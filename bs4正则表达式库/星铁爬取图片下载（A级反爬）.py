import requests
from bs4 import BeautifulSoup
#原神官方网站

# search=input("请输入你要搜索的壁纸：")
search="星壁纸"
#1.获取主页源代码，破解反爬
url = f"https://www.miyoushe.com/sr/search?keyword={search}"
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0"
}
# print(url)
main_response = requests.get(url,headers=headers)
main_response.encoding='utf-8'#处理乱码
main_response_text = main_response.text
print(main_response_text)

#2.通过主页面获取子页面链接
main_page=BeautifulSoup(main_response_text,"html.parser")

# child_response

#2.用bs4拿到主页面的子页面链接



