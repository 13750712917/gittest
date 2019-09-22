#/usr/bin/python
#-*-coding:utf-8-*-

import paramiko
#paramiko 用于远程连接Linux系统、文件下载、上传

#面向过程  ssh协议进行连接、可以执行Linux命令

#创造一个ssh的客户端、
client=paramiko.SSHClient()
#信任远程Linux主机  paramiko.AutoAddPolicy()自动添加信任密文
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#通过客户端连接远程Linux主机
client.connect(hostname='192.168.10.91',
                port=22,
                username='root',
                password='123456'
 )

#执行Linux命令
# exec_command(需要执行的命令):结果是元组
#stdin 输入：ls -al  stdout:输出的结果  stderr:错误信息
stdin,stdout,stderr=client.exec_command('ls -al')
#read()读取
#decode()把  xxx 编译成 xxx     默认（utf-8）
print(stdout.read().decode())

#文件下载 上传
#Transport():作用类似于ftp服务器
ftp = paramiko.Transport(('192.168.10.91',22))

#建立与远程Linux服务器的连接
ftp.connect(username='root',password='123456')
#创建一个类似于ftp的客户端 SFTPClient.from_transport()
sftp = paramiko.SFTPClient.from_transport(ftp)

#下载远程文件 get（参数1，参数2）
#参数1 代表远程文件
#参数2  代表本地文件
x1 ='/opt/自习室'
x2 =r'D:\PycharmProjects\untitled\123\1211\自习室'
sftp.get(x1,x2)

#将本地文件上传到远程Linux服务器
#参数1 代表本地文件
#参数2  代表远程文件位置
x1 =r'D:\PycharmProjects\untitled\123\1211\自习室'
x2 ='/home/自习室'
sftp.put(x1,x2)

#断开连接
ftp.close()
import paramiko
class Paramiko(object):
    def __init__(self,hostname,port,username,password):
        self.hostname=hostname
        self.port=port
        self.username=username
        self.password=password
    def lianjie(self):
        client = paramiko.SSHClient()   #创造ssh对象
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())#信任远程主机、授权
        client.connect(hostname=self.hostname,
                       port=self.port,
                       username=self.username,
                       password=self.password,
                       )
        k = input('输入命令：')
        stdin, stdout, stderr = client.exec_command( k )
        print(stdout.read().decode())
    def get(self):
        ftp = paramiko.Transport((self.hostname, self.port))
        ftp.connect(username=self.username, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(ftp)
        x1 = input('请输入远程文件的位置：')
        x2 = input('请输入本地存储的位置：')
        sftp.get(x1,x2)
    def put(self):
        ftp = paramiko.Transport((self.hostname, self.port))
        ftp.connect(username=self.username, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(ftp)
        x1 = input('请输入本地存储的位置：')
        x2 = input('请输入上传到远程文件的位置：')
        sftp.put(x1,x2)
    def menu(self):
        while True:
            print("""远程控制
            1.执行Linux命令
            2.下载文件
            3.上传文件""")
            choice = input('请选择：')
            if choice =='1':
                print(self.lianjie())
            elif choice =='2':
                print(self.get())
            elif choice =='3':
                print(self.put())
            else:
                print('请输入正确选项')
                continue
k=Paramiko('192.168.10.149' ,22, 'root','123456')
k.menu()







