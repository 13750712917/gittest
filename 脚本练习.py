import pymysql
import xlrd
# c=xlrd.open_workbook(filename=r"C:\Users\WenJinGuo\Desktop\每日一句.xlsx")
# table=c.sheets()[0]
# k=table.nrows
# x=[]
# for i in range(k):
#         a=table.row_values(i)
#         # print(a)
#         x.append(a)
# print(x)
# user_1 = pymysql.connect(
#                 host='192.168.10.126',
#                 port=3306,
#                 user='root',
#                 password='123456',
#                 charset='utf8',
#  )
# d = user_1.cursor()
# sql0='create database 日常 charset="utf8"'
# e = d.execute(sql0)
# sql3='use 日常'
# g = d.execute(sql3)
# sql1 = 'create table  日常.每日一句(日期 char(20),原文 char(150),译文 char(200)) charset="utf8"'
# h = d.execute(sql1)
# for j in  x:
#            sql2 ='insert into  日常.每日一句 values(%s,%s,%s)'
#            e=d.execute(sql2,(j[0],j[1],j[2]))
import time
a=time.localtime()
print(a)