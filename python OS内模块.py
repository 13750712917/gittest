#/usr/bin/python
#-*-coding:utf-8-*-
# OS内模块，作用：python与计算机系统进行交互
import os
# os.getcwd()获取当前目录的路径
print(os.getcwd())
#chdir(路径的名字) 作用：切换路径/目录
os.chdir('1211')
print(os.getcwd())
# .代表当前目录 == os.curdir
print(os.curdir)
# ..代表上一级目录 == os.pardir
print(os.pardir)
os .chdir('..')
print(os.getcwd())#切换到上级目录
# os.name 获取操作系统的类型 Windows Mac uninx Linux
# print(os.name)
#创建多级目录 os.makedirs("多级目录") a/b/c/
# os.makedirs('A/B/C')
#创建一个目录 os.mkdir("目录名字")
# os.mkdir('kkkk/www')
# 删除多个目录，目录必须是空的 removedirs('目录名字')
# os.removedirs('A/B/C')
#删除单个目录：目录必须是空的 rmdir（"目录名字"）
# os.rmdir('kkkk')
#查看当前路径下所有文件、目录 os .listdir('路径名字')    注意：Windows系统路径前面必须加一个小写  r
# d= os.listdir(r'D:\PycharmProjects\untitled\123\1211')
# print(d)
#对文件、目录进行重命名 os.rename('老名字','新名字')
# os.rename(r'D:\PycharmProjects\untitled\123\kkkk',r'D:\PycharmProjects\untitled\123\ffff')
#删除文件 os.remove("绝对路径")
# os.remove(r'D:\PycharmProjects\untitled\123\txt')
#执行系统命令 os.popen("需要执行的命令")
# c= os.popen('dir')
# print(c.read)
#os.path 类  对文件的操作 返回文件的路径 、例如绝对路径、相对路径、判断文件、目录
# 1、返回文件的绝对路径 abspath('文件名')
# q=os.path.abspath('lianxi.py')
# print(q)
# 2、返回文件的上一级路径dirname（"目录名"） a/b/c/a.txt --->/a/b/c
# g=os.path.dirname(r'D:\PycharmProjects\untitled\123\模块')
# print(g)
#3、返回当前文件/目录的名字 basename（'路径'）
# d =os.path.basename(r'D:\PycharmProjects\untitled\123\lianxi.py')
# print(d)
#4、判断文件/目录是否存在 ---> True  False exists("路径")
# print(os.path.exists('lianxi.py'))
#5、判断是否是目录 ---> True  False  isdir("路径名")
# q=os.path.isdir(r'D:\PycharmProjects\untitled\123')
# print(q)
#6、判断是否是文件  ---->  True  False   isfile("路径名")
# f=os.path.isfile(r'D:\PycharmProjects\untitled\123\lianxi.py')
# print(f)
#7、判断是否是链接文件  ---> True False  islink("路径名")
# k=os.path.islink(r'D:\PycharmProjects\untitled\123\lianxi.py')
# print(k)
#8、路径拼接 join('路径一'，'路径二') A B ---> /A/B
# a  = '_'
# b  = '123213'
# print(a.join(b))
# print(os.path.join('/A/','B'))
#9、路径分离 将最后一个文件/目录分离    split ("路径的名字")
# print(os.path.split(r'D:\PycharmProjects\untitled\123\lianxi.py'))
#10、分割文件的后缀名 返回一个元组 splitext('文件名')
 # k= os.path.splitext('lianxi.py')
# print(k)
#统计  顶级目录下有多少个目录,文件个数
