#smtplib email 用于接收、发送邮件
'''
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
class Emil(object):
    def denglu(self):
        # 服务器端的信息
        # 服务器端口号
        self.mail_port = 465
        # 邮件服务器的地址
        self.mail_host = 'smtp.163.com'
        # 邮箱账号
        self.mail_user = '137XXXX2917@163.com'
        # 邮箱密码
        self.mail_pass = '12345678'

        # 发送方地址信息
        self.sender = '137XXXX2917@163.com'
        # 接收方地址信息
        self.receivers = ['135XXX8273@163.com']
    def xie(self):
        # 邮件主题
        self.subject ='2019.8.5日报'
        # 邮件正文内容
        content = '使用Python面向对象发送的邮件。'
        # MIMEText() 类，三个参数。文件内容，文本格式，编码方式
        self.message = MIMEText(content, 'plain', 'utf-8')
    def toubu(self):
        #Header()类，对发送的邮件添加头部信息
        self.message['From'] = Header(self.sender)  # 1.添加发送者头部
        self.message['To'] = Header(str(';'.join(self.receivers)))  # 接收者头部
        self.message['Subject'] = Header(self.subject)  # 添加邮箱的主题
    def fasong(self):
        # 连接邮件服务器并发送邮件
        s = smtplib.SMTP_SSL(host=self.mail_host, port=self.mail_port)  # 登录邮箱
        s.login(self.mail_user, self.mail_pass)  # 输入邮箱账号、密码
        s.sendmail(self.sender, self.receivers, self.message.as_string())  # 发送邮件
        print('邮件发送成功！')
        s.quit()  # 退出邮箱 close仅仅断开连接，quit退出界面



#带附件发送
message=MIMEMultipart()#作用是将正文和附件添加进去并发送出去
#发送邮件
message['From']=Header(sender)#1.添加发送者头部
message['To']=Header(str(';'.join(receivers)))#接收者头部
message['Subject']=Header(subject)#添加邮箱的主题

#准备要发送的正文，HTML文件
with open(file='Hello.html',mode='r',encoding='utf-8')as f:
    content=f.read()
#设置HTML格式
p1=MIMEText(content,'Hello.html','utf-8')
#准备要发送的附件
with open(file='Hello.txt',mode='r',encoding='utf-8')as f:
    d=f.read()
p2=MIMEText(d,'plain','utf-8')
#将文本转成二进制流
p2['Comtent-Type']='application/octet-stream'
#对附件添加一个名字
p2['Content-Disposition'] = 'attachment;filename="Hello.txt"'
#添加照片
with open(file='001.png',mode='rb')as f:
    p3=MIMEImage(f.read())#MIMRImage() 加载二进制图片
p3['Comtent-Type']='application/octet-stream'
p2['Content-Disposition'] = 'attachment;filename="001.png"'

#将三部分附件添加到邮件
message.attach(p1)
message.attach(p2)
message.attach(p3)
#连接邮件服务器并发送邮件
s=smtplib.SMTP_SSL(host=mail_host,port=mail_port)#登录邮箱
s.login(mail_user,mail_pass)#输入邮箱账号、密码
s.sendmail(sender,receivers,message.as_string())#发送邮件
print('邮件发送成功！')
s.close()#退出邮箱   quit() 也可以。close仅仅断开连接，quit退出界面
'''
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

        # 服务器端的信息
        # 服务器端口号
mail_port = 465
        # 邮件服务器的地址
mail_host = 'smtp.163.com'
        # 邮箱账号
mail_user = '137XXX2917@163.com'
        # 邮箱密码
mail_pass = '121234567834'

        # 发送方地址信息
sender = '1375XXX917@163.com'
        # 接收方地址信息
receivers = ['135XXX8273@163.com']

        # 邮件主题
subject ='2019.8.5日报'
        # 邮件正文内容
content = '使用Python面向对象发送的邮件。'
        # MIMEText() 类，三个参数。文件内容，文本格式，编码方式
message = MIMEText(content, 'plain', 'utf-8')

        #Header()类，对发送的邮件添加头部信息
message['From'] = Header(sender)  # 1.添加发送者头部
message['To'] = Header(str(';'.join(receivers)))  # 接收者头部
message['Subject'] = Header(subject)  # 添加邮箱的主题
        # 连接邮件服务器并发送邮件
s = smtplib.SMTP_SSL(host=mail_host, port=mail_port)  # 登录邮箱
s.login(mail_user, mail_pass)  # 输入邮箱账号、密码
s.sendmail(sender, receivers,message.as_string())  # 发送邮件
print('邮件发送成功！')
# s.quit()  # 退出邮箱 close仅仅断开连接，quit退出界面



#带附件发送
message=MIMEMultipart()#作用是将正文和附件添加进去并发送出去
#发送邮件
message['From']=Header(sender)#1.添加发送者头部
message['To']=Header(str(';'.join(receivers)))#接收者头部
message['Subject']=Header(subject)#添加邮箱的主题

#准备要发送的正文，HTML文件
with open(file='Hello.html',mode='r',encoding='utf-8')as f:
    content=f.read()
#设置HTML格式
p1=MIMEText(content,'Hello.html','utf-8')
#准备要发送的附件
with open(file='Hello.txt',mode='r',encoding='utf-8')as f:
    d=f.read()
p2=MIMEText(d,'plain','utf-8')
#将文本转成二进制流
p2['Comtent-Type']='application/octet-stream'
#对附件添加一个名字
p2['Content-Disposition'] = 'attachment;filename="Hello.txt"'
#添加照片
with open(file='001.png',mode='rb')as f:
    p3=MIMEImage(f.read())#MIMRImage() 加载二进制图片
p3['Comtent-Type']='application/octet-stream'
p2['Content-Disposition'] = 'attachment;filename="001.png"'

#将三部分附件添加到邮件
message.attach(p1)
message.attach(p2)
message.attach(p3)
#连接邮件服务器并发送邮件
s=smtplib.SMTP_SSL(host=mail_host,port=mail_port)#登录邮箱
s.login(mail_user,mail_pass)#输入邮箱账号、密码
s.sendmail(sender,receivers,message.as_string())#发送邮件
print('邮件发送成功！')
s.close()#退出邮箱   quit() 也可以。close仅仅断开连接，quit退出界面
