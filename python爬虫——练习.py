#/usr/bin/python
#-*-coding:utf-8-*-
import re
import requests
x={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
r= requests.get(url='https://www.qiushibaike.com/pic/',headers=x)
data=r.content.decode(encoding='utf-8')
# print(data)
a=re.compile(r'<img src="//(.*?)" ')
b=re.findall(a,data)
# print(b)
urls=[]
for i in b:
     urls.append('https://'+i)
     # print(urls)
     # g=0
     for j in urls:
          # print(j)

# for i in list(b):
#     # print(i)
#      # k=list(i)
#      #   for j in (i):
#         urls.append('https:'+i)
#         print(urls)

            # for n in urls:
           #    print(n)
              g =0
              req=requests.get(url=j,headers=x)
              jiegou = req.content  # 图片 二进制
           #  # #     # 保存图片
              f = open(file=f'{g}.jpg', mode='wb')
              f.write(jiegou)
              g+= 1

            # print(n)



