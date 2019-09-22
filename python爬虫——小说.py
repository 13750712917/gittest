#/usr/bin/python
#-*-coding:utf-8-*-

# 爬虫框架   scrapy
"""
爬虫：通过python代码获取网络存放的数据资源 【文件、图片、mp3】
反爬虫：防止资源被爬虫代码获取
反爬机制：属于反爬虫的技术手段之一
最常见的反爬机制：
1、封IP地址
2、封物理网卡的mac地址
3、验证码
4、服务器传输给浏览器的数据通过异步加载。
"""
"""
re模块
requests python发送http/https请求  ，接收响应数据的一个第三方库
"""
import  re
import requests,pymysql
"""
User-Agent:代表浏览器
"""
x ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
#get请求  获取资源
#第一步：发送请求
# r=requests.get(url='https://www.fpzw.com/xiaoshuo/87/87590/17125664.html', headers=x)
#第二步：获取响应的结果、数据
"""
content获取请求之后的响应数据
"""
# data=r.content.decode(encoding='gbk')
#  print(data)
# a=re.compile(r'<h2>(.*?)</h2>')
# b=re.findall(a,data)
# print(b)
# c=re.compile(r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />')
# f=re.findall(c,data)
# print(f)
#"<h2>(.*?)</h2>" ctrl +  f  搜索
# k=open(file='b.txt',mode='w',encoding='utf-8')
# for i in f:
#     print(k.write(f'{i}\n'))


url=requests.get(url='https://www.fpzw.com/xiaoshuo/87/87590')
b = url.content.decode(encoding='gbk')
r0=re.compile(r'<dd><a href="(.*?)">(.*?)</a></dd>')
k=re.findall(r0,b)#获取所有的章节地址和章节名

a=pymysql.connect(host='192.168.10.102',port=3306,user='root',password='123456',charset='utf8')
b=a.cursor()
sql1='create database 小说 charset="utf8"'#创建库
sql2='use 小说'
sql3='create table 小说.小说(章节 text,内容 text)'
b.execute(sql1)
b.execute(sql2)
b.execute(sql3)

for i in range(20):
    url2=requests.get(url=f'https://www.fpzw.com/xiaoshuo/87/87590/{k[i][0]}')
    b1=url2.content.decode('gbk')
    r1=re.compile(r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />')
    k2=re.findall(r1,b1)
    # print(k[i][1])
    # for j in range(len(k2)):
    #     print(k2[j])
    sql4='insert into 小说.小说 values(%s,%s)'
    b.execute(sql4,(k[i][1],''))
    print(k[i][1])
    for j in range(len(k2)):
        sql5='insert into 小说.小说 values(%s,%s)'
        b.execute(sql5,('',k2[j]))



'''

r1=re.compile(r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />')
k=re.findall(r1,b)
# print(k)
a=pymysql.connect(host='192.168.10.54',port=3306,user='root',password='123456',charset='utf8')
b=a.cursor()
sql1='create database 小说 charset="utf8"'
sql2='use 小说'
sql3='create table 小说(章节 text,内容 text) charset="utf8"'
b.execute(sql1)
b.execute(sql2)
b.execute(sql3)
for i in k:
    # print(i)
    sql4='insert into 小说.小说 values(%s,%s)'
    b.execute(sql4,('',i))'''