#/usr/bin/python
#-*-coding:utf-8-*-
# class Excel (object):
# f =open(file= 'a.txt' ,encoding='utf-8')
# a =[ ]
# k=(f.read())
# d= k.replace("(",'').replace(';','').replace('\n','').split(')')
# for i in  d:
#     a.append(i.replace("'",'').split(','))
# import xlwt
# d =xlwt.Workbook()
# table =d.add_sheet("表一")
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         table.write( i,j,a[i][j])
# d.save('kkk.xls')
# import os
# os.chdir(r'D:.')
# k= os.listdir ( r'D:.' )
# print(k)
# q = [ ]
# e = [ ]
# for i in  k:
#     r=os.path.isdir(i)
#     if r==True:
#         q.append(i)
#     else:
#         e.append(r)
#
# print(len(q))
class  Xinxi(object):
    import pymysql
    d = pymysql.connect(
        host='192.168.10.60',
        port=3306,
        user="root",
        password="123456",
        charset="utf8",
        database="1903test",
    )
    e = d.cursor()
    def  jianbiao(self):
        sql7 = "create table xinxi (ID int(20),公司 char(20),职位 char(20), 网址 char(50), 公司类型 char(30), 是否上市 char(20),规模 char(20),地址 char(30), 工作经验 char(20), 学历 char(10))"
        print(self.e.execute(sql7))
    def  xieru(self):
        f = open(file='a.txt', encoding='utf-8')
        c = []
        k = f.readlines()
        for i in k:
            a = i.replace(';', '').replace('\n', '').replace("'", '').replace('(', '').replace(')', '')
            b = a.split(',')
            c.append(b)
        c.pop(len(c) - 1)
        for i in c:
            i.pop(len(i) - 1)
        for j  in i:
            sql3 = f"insert into 1903test.xinxi value {j}"
            self.e.execute(sql3)
            self.d.commit()
k =Xinxi()
k.jianbiao()
k.xieru()








