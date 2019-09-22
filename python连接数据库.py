#/usr/bin/python
#-*-coding:utf-8-*-
import pymysql#导入pymysql第三方库
#第一步与mysql建立连接  connect():建立连接
d=pymysql.connect(
    host='192.168.42.92', # 数据库所在的主机IP地址/域名【云服务器--mysql数据库】
    port=3306,              # mysql的端口号
    user="root",           # mysql的用户名
    password="123456",     # mysql的用户密码，授权密码
    charset="utf8",      # mysql数据的编码方式
    # database ="1903test",    # 指定数据库，不写这个参数，默认使用所有的数据库
)
#第二步：创建一个游标,类似于mysql进入命令行模式 mysql >select * from xx;
e = d.cursor()
#第三步：写SQL语句
# # sql = 'show databases'
# #第四步：执行sql语句 execute(放入需要执行的sql语句)：作用就是执行sql
# #e.executemany(sql语句) #执行多条sql语句
# # data=e.execute(sql)
# # print(data)
# #第五步查询具体结果
"""
a:先找到游标
b：再找到fethch xx()
"""
# e.fetchall() #获取执行sql的所有结果
# e.fetchone() #获取执行sql之后的第一个结果
# e.fetchmany(数字)  #  3  获取执行sql之后的前3条结果
# print(e.fetchall())
# 创建一个库
# sql1 = "create database kkk character set utf8"
# e.execute(sql1)
#创建一个表
# sql2 ="create table user(ID char(20),name char(20))"
# e.execute(sql2)
#数据插入 单引号不能套双引号、双引号可以套单引号
# a = (('3','zhao'),('4','li'),('5','zhang'))
# sql3="insert into user values('2','wang'),('3','zhao'),('4','li')"#插入多条的话后面用逗号隔开
# e.execute(sql3)
# d.commit()#保存到数据库
"""
a:找到连接
b：使用commit()  ---->保存数据到数据库
"""
#更新操作
# sql5 = "update user set ID='4' where name='zhao'"
# e.execute(sql5)
# d.commit()
#删除表中数据
# sql6 = "delete from  user where name='?'"
# e.execute(sql6)
# d.commit()
# class  Xinxi(object):


# sql7 = "create table xinxi (公司 char(20),职位 char(20), 网址 char(50), 公司类型 char(30), 是否上市 char(20),规模 char(20),地址 char(30), 工作经验 char(20), 学历 char(10))"
# e.execute(sql7)
