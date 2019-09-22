#九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f'{i}*{j}={i*j}',end=" ")
#     print(' ')

#字符串转数值
# a='68647953357'
# b=a[::-1]
# c=0
# for i,j in enumerate(b):
#     for k in range(10):
#         if str(k)==j:
#             c=c+k*10**i
# print(type(c))
# print(c)

#创建目录，在目录里创建文件，写入数据，删除文件，删除目录
# import os
# os.mkdir('aaa')#创建文件夹
# os.chdir('aaa')
# a=open(file='a.txt',mode='a',encoding='utf-8')
# a.write('你好！\n')
# a.write('我不好\n')
# a.write('为什么不好\n')
# a.write('就是不好，没理由')
# os.remove(r'E:\.py\day\aaa\a.txt')
# os.rmdir(r'E:\.py\day\aaa')

#连接数据库
# import pymysql
# a=pymysql.connect(host='192.168.10.110',port=3306,user='root',password='123456',charset='utf8')
# b=a.cursor()
# sql1='create database 考试 charset="utf8"'
# sql2='use 考试'
# sql3='create table 考试(a1 text,a2 text,a3 text,a4 text)'
# b.execute(sql1)
# b.execute(sql2)
# b.execute(sql3)
# a1=open(file='Hello.txt',mode='r')
# b1=a1.readlines()
# for i in b1:
#     d=i.replace('\n','')
#     c=d.split(',',)
#     print(c)
#     sql4='insert into 考试.考试 values(%s,%s,%s,%s)'
#     b.execute(sql4,(c[0],c[1],c[2],c[3]))

#统计文件中的除单行注释和空行的行数
# a=open(file="a1.txt",mode='r',encoding='utf8')
# b=a.readlines()
# b1=[]
# for i in b:
#     c=i.replace('\n','')
#     if len(c) !=0 and c[0] !='#':
#         b1.append(c)
# print(len(b1))

#爬虫，糗事百科写入a2.txt
# import requests
# a=requests.get(url='https://www.qiushibaike.com/text/')
# b=a.content.decode(encoding='utf8')
# import re
# c=re.compile(r'<span>\n\n\n(.*?)\n\n</span>')
# d=re.findall(c,b)
# a1=open(file='a2.txt',mode='a',encoding='utf8')
# for i in d:
#     b1=i.replace('<br/>','')
#     b2=b1.replace(' ','')
#     a1.write(f'{b2}\n')

'''
#3.招聘
import pymysql,re,requests
a=requests.get(url='https://sou.zhaopin.com/?jl=653&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3')
b=a.content.decode(encoding='utf8')
print(b)
r1=re.compile(r'<p>(.*?)<span class="salary">(.*?)</span></p>')
r2=re.compile(r'<p class="job-text">(.*?)<span class="vline"></span>(.*?)<span class="vline"></span>(.*?)</p>')
r3=re.compile(r'alt="">(.*?) <span class="user-text"')
a1=re.findall(r1,b)#职位、工资
a2=re.findall(r2,b)#地点、经验、学历
a3=re.findall(r3,b)#公司名
print(a1)
print(a2)
print(a3)
b1=pymysql.connect(host='192.168.10.149',port=3306,user='root',password='123456',charset='utf8')
c1=b1.cursor()
sql1='create database 招聘 charset="utf8"'
sql2='use 招聘'
sql3='create table 招聘(公司名 text,地点 text,职位 text,工资 text,经验 text,学历 text)'
c1.execute(sql1)
c1.execute(sql2)
c1.execute(sql3)
for i in range(len(a3)):
    sql4='insert into 招聘.招聘($s,%s,%s,%s,%s,%s)'
    c1.execute(sql4,(a3[i],a2[i][0],a1[i][0],a1[i][1],a2[i][1],a2[i][2]))
'''

#4.连接Linux主机
# import paramiko
# while True:
#     client = paramiko.SSHClient()
#     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     client.connect(hostname='192.168.10.149',port=22,username='root',password='123456')
#     k = input('输入命令:')
#     stdin, stdout, stderr = client.exec_command( k )
#     print(stdout.read().decode())

#5.发送邮件
# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
# from email.mime.multipart import MIMEMultipart
# from email.mime.image import MIMEImage
# mail_port = 465
# mail_host = 'smtp.163.com'
# mail_user = '13750712917@163.com'
# mail_pass = 'qwer1234tyuiop'
# sender = '13750712917@163.com'
# receivers = ['18317822978@163.com']
# subject ='2019.8.18 考试'
# content = '使用Python面向对象发送的邮件。'
# message = MIMEText(content, 'plain', 'utf-8')
# message['From'] = Header(sender)
# message['To'] = Header(str(';'.join(receivers)))
# message['Subject'] = Header(subject)
# s = smtplib.SMTP_SSL(host=mail_host, port=mail_port)
# s.login(mail_user, mail_pass)
# s.sendmail(sender, receivers,message.as_string())
# s.quit()
# message=MIMEMultipart()
# message['From']=Header(sender)
# message['To']=Header(str(';'.join(receivers)))
# message['Subject']=Header(subject)
# with open(file='Hello.html',mode='r',encoding='utf-8')as f:
#     content=f.read()
# p1=MIMEText(content,'Hello.html','utf-8')
# with open(file='Hello.txt',mode='r',encoding='utf-8')as f:
#     d=f.read()
# p2=MIMEText(d,'plain','utf-8')
# p2['Comtent-Type']='application/octet-stream'
# p2['Content-Disposition'] = 'attachment;filename="Hello.txt"'
# with open(file='001.png',mode='rb')as f:
#     p3=MIMEImage(f.read())
# p3['Comtent-Type']='application/octet-stream'
# p2['Content-Disposition'] = 'attachment;filename="001.png"'
# message.attach(p1)
# message.attach(p2)
# message.attach(p3)
# s=smtplib.SMTP_SSL(host=mail_host,port=mail_port)
# s.login(mail_user,mail_pass)
# s.sendmail(sender,receivers,message.as_string())
# print('邮件发送成功！')
# s.quit()

#写Excel表格
# import pymysql
# import xlwt
# a=pymysql.connect(host='192.168.10.149',port=3306,user='root',password='123456',charset='utf8',database='日常')
# b=a.cursor()
# sql1=('select * from 日常.每日一句')
# b.execute(sql1)
# c=b.fetchall()
# # print(c)
# a1=xlwt.Workbook()
# a2=a1.add_sheet('招聘')
# for i in range(len(c)):
#     for j in range(len(c[i])):
#         a2.write(i,j,c[i][j])
# a1.save('每日一句1.xlsx')

#判断日期
# s = 0
# a = input("请输入:")       # 2019-8-18
# b = a.split('-')
# if int(b[0]) % 400 == 0 or (int(b[0]) % 4 ==0 and int(b[0]) % 100 != 0):
#     day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     for i in range(int(b[1])- 1):
#         s += day[i]
#     s += int(b[2])
#     a = ['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
#     c = s % 7
#     print(f"{b[0]}年是闰年,是一年的第{s-1}天，今天是{a[c]}")
# else:
#     day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     for i in range(int(b[1])- 1):
#         s += day[i]
#     s += int(b[2])
#     a = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
#     c = s % 7
#     print(f"{b[0]}年不是闰年,是一年的第{s-1}天，今天是{a[c]}")




























