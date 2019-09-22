#/usr/bin/python
#-*-coding:utf-8-*-
import  re
import requests
class  Price(object):
    #类属性
    x = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    def __init__(self):
        # 对象属性
        #发送请求
        #发送属性
        r =requests.get(url='https://www.51miz.com/shipin/0-1-0-1.html?utm_term=1349533&utm_source=baidu',headers=self.x)
        #对象属性
        self.d = r.content.decode(encoding='utf8')
    def fenxi(self):
        #先打印一下源html文件
        # print(self.d)
        #写正则
        r1=re.compile(r'<img src="(.*?)" class="show-area-pic"')
        data =re.findall(r1,self.d)
        print(data)
        urls=[ ]
        for i in data:
            urls.append('https:'+i)
            print('https:'+i)
        return urls  #返回值
          # print(data)
    def download(self):
         n=0
         for i  in self.fenxi(): #urls:4个图片的url
             req=requests.get(url=i,headers=self.x)
             #接收响应
             jiegou =req.content  #图片 二进制
            #保存图片
             f=open(file=f'{n}.jpg',mode='wb')
             f.write(jiegou)
             n+=1



k=Price()
k.download()

