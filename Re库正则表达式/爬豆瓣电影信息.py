import re
def findall_match():
    # findall: 匹配字符串中所有的符合正则的内容
    lst = re.findall(r"\d+","我的电话号是:10086，我女朋友的电话是:10010")
    print(lst)

def finditer_match():
    # finditer:匹配字符串中所有的内容[返回的是迭代器]，从迭代器中拿到内容需要，一般用这个效率高
    it= re.finditer(r"\d+","我的电话号是:10086，我女朋友的电话是:10010")
    for i in it:
        print(i.group())

def search_match():
    # search，找到一个结果就返回，返回的结果是match对象，拿数据需要.group()
    s = re.search(r"\d+","我的电话号是:10086，我女朋友的电话是:10010")
    print(s.group())

def match_match():
    # match是从头开始匹配,如下如果匹配不到就会报错
    s = re.match(r"d+","10086，我女朋友的电话是:10010")
    print(s.group())

def compile_match():
    # 预加载正则表达式
    obj = re.compile(r"\d+")#相当于算法
    ret = obj.finditer("我的电话号是:10086，我女朋友的电话是:10010")
    for it in ret:
        print(it.group())
    ret = obj.findall("我的电话号是:10086，我女朋友的电话是:10010")
    print(ret)




def most_important_use():
    """
    最常用的的Re正则表达式：筛选页面源代码的信息
    惰性匹配->就近原则：.*?
    活性匹配->全部:.*
    捕抓的内容放到迭代器：?P<数组名字>
    :return:
    """
    S="""
        <div class=' jola'><span id='1'>郭麒麟</span></div> 
        <div class=' jolb'><span id='2'>宋铁</span></div> 
        <div class=' jolc'><span id='3'>范思哲</span></div> 
        <div class=' jold'><span id='4'>胡说八道</span></div> 
    """
    #获取类名、id、人名
    # obj1=re.compile(r"<div class='.*?'><span id='\d+'>.*?</span></div>",re.S)#预编译算法，用'别用",re.S是为了让.匹配还行符号
    obj1 = re.compile(r"<div class='(?P<class_name>.*?)'><span id='(?P<id>\d+)'>"
                      r"(?P<name>.*?)</span></div>", re.S)#直接分组
    result = obj1.finditer(S)
    for it in result:
        print("类名是:",it.group("class_name").strip()," id是:",it.group("id")," 人名是:",it.group("name"))#strip类名去前后空格


import requests
import csv
def Get_Douban_movies_Re_regular_expression(creathtml=False,creatcsv=False):
    """
    获取豆瓣网页的数据：服务器渲染
    把网页源代码写进test文件
    把数据写进csv文件
    :param creathtml:
    :param creatcsv:
    :return:
    """
    url="https://movie.douban.com/top250"
    #破反爬
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0"
    }
    response = requests.get(url,headers=headers)
    #直接生成文档
    if creathtml:
        with open("../test.html", 'w', encoding='utf-8') as f:
            f.write(response.text)
    #输出源代码
    print(response.text)
    #正则表达->惰性匹配->筛选信息：
    obj = re.compile(
        r'<li>.*?<div class="item">.*?<span class="title">(?P<movie_name>.*?)</span>'
        '.*?导演: (?P<dictor>.*?) .*?<br>(?P<time>.*?)&nbsp.*?property="v:average">(?P<score>.*?)</span>.*?'
        r'<span>(?P<nums>.*?)人评价', re.S)
    #匹配+返回迭代器
    result=obj.finditer(response.text)
   #迭代器用完一次就报废，哎只能以这种形式一次性存在
    if creatcsv:
        #把数据写进去csv
        with open("../test.csv", 'w', encoding='utf-8') as f:
            csvwriter = csv.writer(f)
            # 遍历迭代器写入csv文件
            for it in result:
                # 先把数据转换字典
                mydict = it.groupdict()
                # 再把数据去前后空格再赋值
                mydict['movie_name'] = mydict['movie_name'].strip()
                mydict['dictor'] = mydict['dictor'].strip()
                mydict['time'] = mydict['time'].strip()
                mydict['score'] = mydict['score'].strip()
                mydict['nums'] = mydict['nums'].strip()
                # 格式化字典后写入csv文件
                csvwriter.writerow(mydict.values())
    else:
        for it in result:
            # 输出对齐
            print("电影名称:", it.group('movie_name').strip().ljust(10),
                  "主要导演:", it.group('dictor').strip().ljust(10),
                  "上演时间:", it.group('time').strip().ljust(10),
                  "大众评分:", it.group("score").strip().ljust(10),
                  "评论人数:", it.group('nums').strip().ljust(10))
    response.close()



Get_Douban_movies_Re_regular_expression(True,True)


