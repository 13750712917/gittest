import  re
import requests
x={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
r=requests.get(url='https://www.fpzw.com/xiaoshuo/87/87590/',headers=x)
b = r.content.decode(encoding='gbk')
# print(b)
r=re.compile(r'<dd><a href="(.*?)">(.*?)</a></dd>')
a=re.findall(r,b)
# print(a)
k=open(file=r'e:/雪鹰领主.txt.',mode='a',encoding='utf-8')
for i in range (100):
    # print(i[0])
    url1=r=requests.get(url='https://www.fpzw.com/xiaoshuo/87/87590/'+a[i][0],headers=x)
    b1 = r.content.decode(encoding='gbk')
    r1=re.compile(r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br /><br />')
    a1=re.findall(r1,b1)
    k.write(f'{a[i][1]}\n')
    for j in a1:
        k.write(f'{j}\n')
    print(f'{a[i][1]}完成!')

from selenium import webdriver
dr=webdriver.Firefox()
dr.get('http://jz1.jingjichina.com.cn/')
