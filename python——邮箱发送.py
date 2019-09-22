#/usr/bin/python
#-*-coding:utf-8-*-
#python smtplib email 作用：用于接受、发送邮件
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
#设置服务器端的信息

mail_host='smtp.163.com'

# 邮件服务器端口号
mail_port = 465
#用户信息

mail_user='13525038273@163.com'

#用户授权码

mail_pass='wang12345'

#发送信息

# 邮件发送方地址
sender ="13525038273@163.com"
#邮件接受方的地址
receivers=['13750712917@163.com','15206265349@163.com'] #可以多个

#邮件正文

#设置邮件的主题
subject = "2019.8.15日报"

#设置邮件正文
# content ="学习python—邮箱发送"

#三个参数 ：第一个为文本内容  ,第二个plain设置文本格式 ， 第三个 utf-8设置编码
#MIMEText()类
# message =MIMEText(content,'plain','utf-8')
"""
Header()类，作用：对发送的邮件添加头部信息
"""
#发送邮件的过程
#第一步：添加发送者头部
# message['From']=Header(sender)
#第二步：添加接受者头部
# message['To']=Header(str(";".join(receivers)))
#第三步：添加邮件的主题
# message['Subject']=Header(subject)


#连接邮件服务器，并发送邮件
#第一步：登录邮箱
# s=smtplib.SMTP_SSL(host=mail_host,port=mail_port)
#第二步：输入账号密码
# s.login(mail_user,mail_pass)
#第三步：发送邮件
# s.sendmail(sender,receivers,message.as_string())
# print('邮件发送成功')
#第四步：退出登录
# s.close()#只是断开连接，没有退出服务器页面
# s.quit()退出整个发送邮箱的服务器，减少计算机内存


#带有附件的邮件发送
#添加一个MIMEMUltipart类；
#作用：将正文及附件添加到邮件里
message=MIMEMultipart()

#发送邮件的过程
#第一步：添加发送者头部
message['From']=Header(sender)
#第二步：添加接受者头部
message['To']=Header(str(";".join(receivers)))
#第三步：添加邮件的主题
message['Subject']=Header(subject)

#准备要发送的正文、使用htnl格式的正文内容，添加附件

with open(file='日报总结.html',mode='r',encoding='utf-8')as f:
    content =f.read()

#设置html格式
p1=MIMEText(content,'html','utf-8')

#准备一个要发送的附件
with open(file='hell.txt',mode='r',encoding='utf-8')as f:
    d=f.read()

#设置txt格式
p2=MIMEText(d,'plain','utf-8')

#将文本转至二进制流
p2['Content-Type']='application/octet-stream'
#对附件添加一个名字
p2['Content-Disposition'] = 'attachment;filename="hello.txt"'
#添加一个照片作为附件
with open (file='0.jpg',mode='rb')as f:
#MIMEImage()加载二进制图片
    p3 = MIMEImage(f.read())
#将文本转至二进制流
p3['Content-Type']='application/octet-stream'
#对附件添加一个名字
p3['Content-Disposition'] = 'attachment;filename="0.jpg"'

#将三部分添加到邮件里
message.attach(p1)
message.attach(p2)
message.attach(p3)

#连接邮件服务器，并发送邮件
#第一步：登录邮箱
s=smtplib.SMTP_SSL(host=mail_host,port=mail_port)
#第二步：输入账号密码
s.login(mail_user,mail_pass)
#第三步：发送邮件
s.sendmail(sender,receivers,message.as_string())
print('邮件发送成功')
#第四步：退出登录
s.close()#只是断开连接，没有退出服务器页面
# s.quit()退出整个发送邮箱的服务器，减少计算机内存

