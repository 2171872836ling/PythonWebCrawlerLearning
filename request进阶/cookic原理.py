# cookie是首次登陆之后在服务器端生成的一串代码，然后服务器端在返回数据的时候会将cookie返回到客户端储存，下一次登陆的时候会携带该cookie
# 带着这串代码+访问->使用session进行请求：保证访问过程cookic不会丢失
# 注意：cookie是在“登录/退出登录”一瞬间产生的，要在之前抓包，找到一个login的响应
import requests

#会话
#cookic->服务器
#cookic<-服务器
#cookic->服务器
# 1.创建对话
session = requests.session()#类似缓存保存cookie和会话

# 2.用data负载，第一次产生cookie
data={

}












