#/usr/bin/python
#-*-coding:utf-8-*-

#操作Excel的xlrd读取文件 xlwt 写入数据到Excel文件
import xlrd
#第一步：打开Excel
d = xlrd.open_workbook(filename='每日一句.xlsx')

#第二步：选中一个子表 sheet1 ,sheet2
#第一种选中表的方法
# table = d.sheets()[0]
# print(table)
#第二种选中表的方法
# table = d.sheet_by_index(0)
# print(table)

"第三步：获取数据"
#row_values():获取整行数据，必须指定获取的行号
# a = table.row_values(0)
# print(a)
#col_values():获取整列的数据，必须指定获取的列号
# a = table.col_values(0)
# print(a)
#获取某一个单元格的值
# row()获取某一行  -->返回的是一个列表
#再通过列表的索引获取到元素  ——.value  获取到具体的值
# print(table.row(0)[0].value)
#先获取一列 col() -->返回一个列表
#在通过列表的索引获取到元素 -->.value 获取到具体的值
# print(table.col(0)[1].value)
#通过行、列索引获取到具体单元格的值
 # print(table.cell(0,2).value)
#获取行数、列数
"""
nrow:获取的是行数
ncols：获取的是列数
"""
# print(table.nrows)
# print(table.ncols)
# 如何获取行数据？
# k=table.nrows
# for i in  range(k):
#     a = table.row_values(i)
#     print(a)

#sheet_name():找出文件中所有的表的名字
# print(d.sheet_names())
"""
定义一个类：
1、可以打开不同的Excel文件
2、按照行读取任意行数据 2 - 3
3、读取指定单元格的数据  0， 4
4、按照列读取任意行数据 2 - 3
5、指定读取某个表格的数据
"""
# class Excel(object):
#     k = input('输入想要打开的Excel文件：')
#     import xlrd
#     d = xlrd.open_workbook(filename= k)
#     h = int(input('输入要打开的子表：'))
#     print(d.sheets()[h-1])
#     def duhang(self):
#         e = int(input('输入要获取数据的行号：'))
#         r = int(input('输入要获取数据的列号：'))
#         print(self.d.row(0)[r-1].value)
#     def  dudan(self):
#         w = int(input('输入要获取数据的行号：'))
#         q = int(input('输入要获取数据的列号：'))
#         print(self.d.cell(w-1,q).value)
'''
class Excel (object):
    def __init__(self,name ,table):#魔法方法 对象属性：文件名、表格
        self.name = name
        self.table = table
        import xlrd
        self.d = xlrd.open_workbook(filename=self.name)#打开文件
        self.t = self.d.sheets()[self.table]
    def _row_(self):
        a = int(input('请输入查询的起始行号：'))
        b = int (input('请输入查询的终止行号：'))
        if a>b:
            if a >self.t.nrows:
                print('超出查询范围')
                return None
            else:
                for i in range(b,a+1):
                    print(self.t.row_values(i))
        else:
            if b >self.t.nrows:
                print('超出查询范围')
                return None
            else:
                for i in range(a,b+1):
                    print(self.t.row_values(i))
    def _col_(self):
        s = int(input('输入查询的起始列号：'))
        f = int(input('输入查询的终止列号：'))
        if s>f:
            if s > self.t.ncols:
                print('超出范围')
            else:
                for j in range(f,s+1):
                    print(self.t.col_values(j))
        else:
            if f > self.t.ncols:
                print('超出范围')
            else:
                for j in range(s,f+1):
                    print(self.t.col_values(j))
    def _cell_(self):
        k = int(input('请输入行号：'))
        m = int(input('请输入列号：'))
        print(self.t.cell(k - 1, m).value)
    def mine(self):
        print('1、读取指定行的数据\n2、读取指定列的数据\n3、读取指定单元格的数据\n4、退出')
        while True:
            chose=int(input('请输入你的选择：'))
            if chose==1:
                self._row_()
            elif chose ==2:
                self._col_()
            elif chose ==3:
                self._cell_()
            elif chose ==4:
                break
            else:
                print('请输入正确的数据')
if __name__ == '__main__':
    q =Excel('wwww.xls',0)
    q.mine()







#新建一个Excel文件
#第一步：新建一个Excel文件
#xlwt.workbook()新建一个文件excel文件
# d =xlwt.Workbook()
#第二步：新建一个Excel表  add_sheet(工作表的名字)表名必填
table =d.add_sheet("表一")
#第三步：写入数据到Excel表中，一次写入一个单元格
#write（行号，列号，要写入的数据）
for i in range(len(a)):
    for j in range(len(a[i])):
        table.write( i,j,a[i][j])
#第四步：保存Excel文件
#save（'Excel文件名'）
d.save('wwww.xls')
'''


















