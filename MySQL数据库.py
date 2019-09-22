# import pymysql
# import xlrd
# a1=pymysql.connect(host='192.168.42.92',user='root',password='123456',charset='utf8',port=3306)
# biao=a1.cursor()
# sql1='create database 日常 charset="utf8"'
# sql2='use 日常'
# sql3='create table 每日一句(日期 text,原文 text,译文 text) charset="utf8"'
# biao.execute(sql1)
# biao.execute(sql2)
# biao.execute(sql3)
# a=xlrd.open_workbook(filename=r'C:\Users\WenJinGuo\Desktop\每日一句.xlsx')
# b=a.sheets()[0]
# c=b.nrows
# for i in range(c):
#     a=b.row_values(i)
#     sql4='insert into 日常.每日一句 values(%s,%s,%s)'
#     biao.execute(sql4,(a[0],a[1],a[2]))

# !/usr/bin/python
# -*-coding:utf-8-*-
import pymysql,xlrd
a=pymysql.connect(host='192.168.42.92',port=3306,user='root',password='123456',charset='utf8')
b=a.cursor()
sql1='create database aaa charset="utf8"'
sql2='use aaa'
sql3='create table bbb(编号 text,姓名 text,性别 text,年龄 text) charset="utf8"'
b.execute(sql1)
b.execute(sql2)
b.execute(sql3)
# a1=xlrd.open_workbook(filename='学生表.xlsx')
# b1=a1.sheets()[0]
# c1=b1.nrows
# for i in range(c1):
#     d=b1.row_values(i)
#     sql4='insert into aaa.bbb values(%s,%s,%s,%s)'
#     b.execute(sql4,(d[0],d[1],d[2],d[3]))