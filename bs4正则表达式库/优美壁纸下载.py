import requests
from bs4 import BeautifulSoup



#1.获取主页源代码
url = f"https://www.umei.cc/e/search/result/?searchid=125"
# print(url)
main_response = requests.get(url)
main_response.encoding='utf-8'#处理乱码
main_response_text = main_response.text
print(main_response_text)

#2.通过主页面获取子页面链接
main_page=BeautifulSoup(main_response_text,"html.parser")
main_page.find("")
# child_response

#2.用bs4拿到主页面的子页面链接



