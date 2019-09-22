#/usr/bin/python
#-*-coding:utf-8-*-

#选择法排序
# a=[2,4,1,5,8,6]
# b=len(a)
# for i in range (b):
#     for j in range(i+1,b):
#        if a[i]>a[j]:
#            a[i],a[j]=a[j],a[i]
# print(a)
# #冒泡法排序
# a=[2,4,1,5,8,6]
# b=len(a)
# for i in range(b):
#     for j in range( b-1):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)
# #质数之和（100以内）
# d=0
# for i in range(2,100):
#     for j in range (2,100):
#         c=i%j
#         if c==0:
#             break
#     if i==j:
#         d=d+i
# print(d)
# #水仙花数
# for i in range (100,1000):
#     q=i//100
#     w=i//10%10
#     e=i%10
#     if i==q**3+w**3+e**3:
#         print(i)
#阶乘之和（任意输入）
# a= int((input('输入任意一个正整数字：'))
# if float(a)>=0:
#     print('无阶乘')
# elif int(a)>=1:
#     print('有阶乘')
# q=0
# for w in range (1,a+1):
#     c=1
#     for t in range (1,w+1):
#         c=c*t
#         q=q+c
# print('阶乘之和为：{}'.format(q))
# import random
# q=('1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm')
# c=[ ]
# for i in range (6):
#     b=random.randint(0,61)
#     r=''.split(q)
#     c.append(q[b])
#     v=''.join(c)
# print(v)
# e=input('输入验证码：')
# if len(e)==6:
#     if v==e:
#         print('你不是瞎子')
#     else :
#         print('看不清')
# else:
#     print('验证码不符合规则')
#
# a='1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
# c=[]
# while 1:
#     for i in range(6):
#         import random
#         b=random.randint(0,len(a)-1)
#         e=c.append(a[b])
#     e=''.join(c)
#     print(e)
#     d=input('请输入验证码:')
#     if len(d)==6:
#         if d==e:
#             print('验证成功!')
#             break
#         else:
#             print('验证失败!')
#     else:
#         print('长度不够6位，验证失败!')
#     c.clear()
#     f=input('还要继续输入验证码吗?(Y/N)')
#     if f=='Y':
# continue
# elif f=='N':
#     print('那好吧,下次再见!')
#     break
# else:
#     g=input('输入错误,只能输入"Y"或"N"!再次确认还要继续吗?')
#     if g=='Y':
#         continue
#     elif g=='N':
#         print('那好吧,下次再见!')
#         break
#          else:
#             print('很抱歉,您又输错了!再见!')
#             break
# a=[1,3,4,7]
# b=1
# for i in range (b):
#     a.insert(len(a),a[0])
#     a.remove(a[0])
#     print(a)
# a=input('请输入一个正整数:')
# b=0
# for i in range(1,int(a)):
#     c=1
#     for j in range (1,i+1):
#         c=c*j
#     b=b+c
# print(b)
# a= int (input('输入任意一个正整数字：'))
# q=0
# for w in range (1,a+1):
#      c=1
#      for t in range (1,w+1):
#          c=c*t
#      q=q+c
# print('阶乘之和为：{}'.format(q))
# import pymysql
# d = pymysql.connect(
#         host = '192.168.2.183',
#         port = 3306,
#         user = "root",
#         password = "123456",
#         charset = "utf8",
#         database = 'hao123'
#     )
# a = d.cursor()
# sql="""create table kebiao(ID int ,name char(20),) """
# try:
# data=a.execute(sql)
# print(data)
# class Book(object):
#
#         def __init__(self, name, author, status, bookindex):
#                 self.name = name
#                 self.author = author
#                 self.status = status
#                 self.bookindex = bookindex
#
#         def __str__(self): #魔法方法的一种，自动将对象的属性
#                 if self.status == 1:
#                         stats = '未借出'
#                 elif self.status == 0:
#                         stats = '已借出'
#                 else:
#                         stats = '状态异常'
#                 return '书名: 《%s》 作者: %s 状态: <%s> 位置: %s' \
#                        % (self.name, self.author, stats, self.bookindex)
#
#
# class BookManage(object):
#         books = []
#
#         def start(self):
#                 self.books.append(Book('python', 'guido', 1, 'ISO9001'))
#                 self.books.append(Book('c', '谭浩强', 1, 'NFS8102'))
#                 self.books.append(Book('java', 'westos', 1, 'PKA7844'))
#                 # 0:借出 1：存在
#                 # python 1
#                 # c 1
#                 # java 1
#
#         def Menu(self):
#                 self.start()
#                 while True:
#                         print("""
#       图书管理系统
#   1.查询图书
#   2.增加图书
#   3.借阅图书
#   4.归还图书
#   5.退出系统
#   """)
#
#                         choice = input('请选择：')
#
#                         if choice == '1':
#                                 self.showAllBook()
#                         elif choice == '2':
#                                 self.addBook()
#                         elif choice == '3':
#                                 self.borrowBook()
#                         elif choice == '4':
#                                 self.returnBook()
#                         elif choice == '5':
#                                 print('欢迎下次使用...')
#                                 exit()
#                         else:
#                                 print('请输入正确选择')
#                                 continue
#
#         def showAllBook(self):
#                 for book in self.books:
#                         print(book)
#
#         def addBook(self):
#                 name = input('图书名称:')
#                 self.books.append(Book(name, input('作者:'), 1, input('存储位置:')))
#                 print('图书《%s》增加成功' % name)
#
#         def checkBook(self, name):
#                 for book in self.books:
#                         if book.name == name:
#                                 return book
#                 else:
#                         return None
#
#         def borrowBook(self):
#                 name = input('借阅图书名称: ')
#                 ret = self.checkBook(name)
#                 print(ret)
#
#                 if ret != None:
#                         if ret.status == 0:
#                                 print('书籍《%s》已经借出' % name)
#                         else:
#                                 ret.status = 0
#                                 print('书籍《%s》借阅成功' % name)
#                 else:
#                         print('书籍《%s》不存在' % name)
#
#         def returnBook(self):
#                 name = input('归还图书名称:')
#                 ret = self.checkBook(name)
#
#                 if ret != None:
#                         if ret.status == 0:
#                                 ret.status = 1
#                                 print('书籍《%s》归还成功' % name)
#                                 print(ret)
#                         else:
#                                 print('书籍《%s》未借出' % name)
#                 else:
#                         print('书籍《%s》不存在' % name)
#
#
# manager = BookManage()
# manager.Menu()
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
# class Email(object):
#         mail_host = 'smtp.163.com'
#         mail_port = 465
#         mail_user = '13525038273@163.com'
#         mail_pass = 'wang12345'
#         sender = "13525038273@163.com"
#         receivers = ['13750712917@163.com', '15206265349@163.com']
#         def xieyoujian(self) :
#                 self.subject = "2019.8.15日报"
#                 content = "学习python—邮箱发送"
#                 self.message = MIMEText(content, 'plain', 'utf-8')
#         def fasong(self):
#                 self.message['From'] = Header(self.sender)
#                 self.message['To'] = Header(str(";".join(self.receivers)))
#                 self.message['Subject'] = Header(self.subject)
#         def lianjie(self):
#                 s = smtplib.SMTP_SSL(host=self.mail_host, port=self.mail_port)
#                 s.login(self.mail_user, self.mail_pass)
#                 s.sendmail(self.sender,self. receivers,self.message.as_string())
#                 print('邮件发送成功')
#                 s.close()
# k = Email()
# k.xieyoujian()
# k.fasong()
# k.lianjie()


