#/usr/bin/python
#-*-coding:utf-8-*-
#a='hello,python'
#print(a)
#a=  '  hello,python  '
#b=a.strip()
#print(b)
#b=a.lstrip()
#print(b)
#b=a.rstrip()
#print(b)
#a='%s是%s个超级大国'%('中国',1)
#print(a)
#a=[12,121,12122,122]
#a.sort()
#print(a)
#a.reverse()
#print(a)
#a=[123,1212,1445]
#b=a.index(123)
#print(b)
#=[1223,233,65,556]
#a.sort()
#print(a)
#a.reverse()
#print(a)
#b=[111,222]
#a.extend(b)
#print(a)
#a.clear()
#print(a)
#a=[123,21323,1321424]
#a.append(111)
#a.insert(1,111)
#a.remove(123)
#print(a)
#一、字符串：以单引号和双引号括起来
#字符串特点：
#1、支持索引
#2、支持切片
#3、不可变的
#a='  hello,python   '
#b=a.upper()#1、将字符串小写变大写
#b=a.lower()#2、将字符串大写变小写
#b=a.title()#3、将字符串的第一个字符首字母大写
#b=a.swapcase()#4、数据反转，大写变小写，小写变大写
#b=a.startswith('h')#5、判断字符串是否是以这个字符开头，如果正确返回ture，错误返回flash
#b=a.endswith('n')6、#判断字符串是否以这个字符结尾，如果正确返回ture，错误，返回flash
#b=a.replace('o','博文',1)7、替换字符串，（‘要替换的内容’，‘替换的内容’，替换数量（数量不用加引号））
#b=a.split('h')#8、将字符串分割成列表（分割字符串列表）
#b='-'.join('6789')#9、形成新的字符串的分隔符（连接成新的字符串）
#a='{}hello,python{}'
#b=a.format('你好','蟒蛇')#10、格式化字符串，占位符{} 变量名.format.(字符串)
#a='%s是%d个超级大国'%('中国',1)#11、%s可以填充所有，%d只能填充数字
#b=a.strip()#12、去除空格
#print(b)
#b=a.lstrip()#去除左边空格
#print(b)
#b=a.rstrip()#去除右边空格
#print(b)
#二 、元组：元组是数据的集合，以小括号标识，中间以逗号隔开
#元组特点：
#1、不可变
#2、支持索引
#3、支持切片
#内置函数练习
#a=(123,1234,567,123)
#b=a.count(123)1、统计这个元素在元组中有多少个
#b=a.index(567)2、查询这个元素在这个元组中的下标位置
#print(b)
#三、列表：列表是一组数据的集合，以中括号标识，中间用逗号隔开
#列表特点：
#1、可变的
#2、支持索引
#3、支持切片
#列表内置函数基础练习
#a=[121,3423,12123]
#a.append(122)1、对列表添加数据，添加后自动在最后面
#a.insert(1,222)2、根据下标进行添加数据
#a.remove(121)3、删除指定数据
#a.pop(1)4、根据下标删除数据
#b=a.count(121)5、统计这个数据在列表中有多少个
#b=a.index(121)6、查询此元素在列表的下标
#b=[111,345]
#a.extend(b)7、将b中的数据更新到a中
#a.clear()8、清空数据
#a.sort()9、排序
#print(a)
#a.reverse()10、数据转换
#b=a.copy()11、复制
#print(b)
#列表和元组的区别？
#1、元组是不可变的，列表是可变的；
#2、元组是以小括号标识的，列表是以中括号标识的；
#3、元组里面只有一个元素时，结尾必须要加逗号，才可以标识元组，而列表不需要；
#四、集合：一组数据的集合，以大括号标识，中间用逗号隔开。
#集合的特点：
#1、集合是无序的；
#2、集合是不可重复的；
#3、可变的；
#集合的内置函数
#a={1332,'hdhjh',123}
#a.add(111)1、添加数据，一次只能添加一个
#print(a)
#五、字典：一组数据的集合，以大括号为标识，格式以键值对出现（key：value）
#字典特点：
#1、无序的
#2、可变的
#3、键必须是唯一的
#字典内置函数基础练习
#a={'姓名':'张三','年龄':'22','性别':'男'}
#b=a.keys()1、获取所有的键
#b=a.values()2、获取所有的值
#b=a.items()3、获取所有的键值对
#a['sex']='111'4、添加数据，有的数据就更改
#a.pop('性别')5、指定删除的数据
#a.popitem()6、删除数据，默认删除最后一个
#b={'sex':'123'}
#a.update(b)7、更新数据，将b的数据更新到a里面
#print(a)
#a=0x20
#print(int(a))
#python if条件语句
#if False:
#   print(12)
#else:
#    print(11)
#a=int(input('输入账号'))
#b=int(input('密码'))
#if a==1761295435:
#    print()
#    if b==123456:
#       print('登录')
#    else:
#        print('密码错误')
#else:
#    print('登录失败')

#加
#a = 100
#b = 20
#d = 'hello,python'
#c=a+b
#print(c)

#减
#c=a-b
#print(c)

#乘
#c=a*b
#print(c)

# 除
#c=a/b
#print(c)#除的结果是浮点型

# 求整数【商的整数】
#c=a//b
#print(c)

#幂
#c=a**b
#print(c)

#求余数
#s1=100
#s2=3
#f=s1%s2
#print(f)

# python 比较运算  两个变量之间值的比较
# ==等于 >大于 <小于 >=大于等于  <=小于等于  ！=不等于
#a=int (input('输入成绩:'))
#if  90<=a<=100:
#    print('优秀')
#elif 80<=a<=90:
#    print('良好')
#elif 60<=a<=80:
#    print('一般')
#elif a<60 :
#    print('不及格')

#python   赋值运算符
#= 赋值 +=累加  -=类减  *=  /=  %=  //=  **=
#a1=100
#a1+=1  #a1=a1+1
#print(a1)

#python成员运算符
#""""""
#in 在...里面
#not in  不在...里面
#x=[1,2,3,4]
#print(1 in x)

#逻辑运算符
#and 与 两个条件同时为True，结果才为Ture
# or 或 有一个条件为Ture，结果就是Ture
#not  非 一个条件，Ture变成False，False变成True

#数值0、空字符串、空列表、空元组、空集合、空字典 默认是False；
#None 空的    函数里面的返回值的一种；
#if  '':
#    print('hello')

#python  for  循环
#循环一个字典的时候，只能拿到它的键
#  for i  in  xx;
#      代码语句
#   xx  代表的是可迭代的对象    字符串，列表，元组，集合，字典
#    i  变量  代表  xx某一个具体的值
#str_1='hello,python' 字符串循环
#for i in str_1:
#    print(i)

#dict_1={1:'python',2:'hello'}字典循环
#for i in dict_1:
#    print(i)

#集合去重
#list_a=[1,2,1,3,4,2,5,1,6,7,4,6,5,3,2]
#list_b=[]
#for i in list_a:
#    if i not in list_b:
#        list_b.append (i)
#print(list_b)

#python九九乘法表
#for i in range(1,10):
#    for a in range (1,i+1):
#        print('{}*{}={}\t'.format(a,i,i*a),end='')
#    print()

"""圈圈小程序
import turtle as t
t.color('red')
for i in range(300):
    t.fd(i)
    t.left(120)
t.done()
"""

#1、将text中每个首字符大写的英文单词添加到一个列表中
"""text = "Early in the day it was whispered that we should sail in a boat, only thou and I, and never a soul in the world would know of this our pilgrimage to no country and to no end"
g=text.split( )
b=[]
for i in g:
    if i.istitle():
        b.append(i)
        print(b)"""



#2、将首字符小写的单词转换为首字符大写
#a=text.title()
#print(a)
#3、将text中所有的包含a的字符替换成博文两个字
#a=text.replace('a','博文')
#print(a)
#4、删除包含小t字符的单词后，组成一个新的字符串
# g=text.split(' ')
# for i in g:
#     if 't' in i:
#         g.remove(i)
#         b=' '.join(g)
# print  ('hello'.find ('e'))

#x="tom猫"
#print(f"你好 {x}")
#:空白字符包含：空白、\n  \t   \r  回车
# a='hello'
# print(a[::-1])
#a=str(input('回文：' ))
#for i in range (0,int(len(a))):
#    if a[i]!=a[-i-1]:
#        print('不是回文')
#        break
#else:
#    print('是回文')
'''a=[1,2,3,4]
b=list(a)
b= a[::-1]
print(b)'''
#a=[8,1,4,6,7]
"""a=list(input('输入数据:'))
b=len(a)
for i in range (b):
    for j in range(b-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)"""
# 统计字符串长度大于5的
# 将e全部替换成博文
# 截取第一个逗号前的所有单词，并将首字符大写
# 删除除包含英文o的单词
s="""Then one day the mother eagle appeared at the top of the mountain cliff, with a big bowl of delicious food and she looked down at her baby. The baby looked up at the mother and cried "Why did you abandon me? I'm going to die any minute.'How could you do this to me?"""
"""统计字符串长度大于5的
b=[]
c=s.split()
for i in c:
    if len(i)>5:
        b.append(i)
        d=len(b)
print(d)"""
"""截取第一个逗号前的所有单词，并将首字符大写；
c=s.split(',')
d=c[0]
e=''.join(d)
f=e.title()
print(f)"""
"""删除除包含英文o的单词
c=s.split(' ')
for i in c:
    if 'o' in i:
        c.remove(i)
        b=' '.join(c)
print(b)"""
# a=[1,3,11]
# for i,j  in enumerate(a):
#     #print(j)
    #print(j)
# a=["面包","火腿","香蕉","苹果","桔子"]
# b=[30,50,20,25,40]
# k=[90,35,20,70,26]
# print('商品编号\t商品名\t\t\t单价')
# for i ,j in enumerate(a):
#     print('{}\t\t\t{}\t\t\t{}'.format(i,j,b[i]))
#     while True:
# c=int (input('请输入商品编号'))
# if  0<=len(a):
#     d=int(input('请输入购买数量:'))
#     if 0<(d):
#         e=input('是否使用会员?(y / n)')
#         if e=='y':
#             f=input('请输入会员卡号:')
#             if f in ['123456','666666']:
#                 print('应付金额为{}元'.format(b[int(c)]*int(d)*0.95))
#             else:
#                 print('会员卡号输入错误!')
#         elif e=='n':
#             print('应付金额为{}元'.format(b[int(c)] * int(d)))
#         else:
#             print('输入无效,只能输入“yes”或"no"')
#     else:
#         print('数量输入错误!')
# else:
#     print('商品号输入错误!')
# 求1,2,3,4，可以组成多少个三位数
# 字符串类型的123456在不使用int()转为数字类型
# a=[1,2,3,4]
# for i in(a):
#     for j in(a):
#         for q in (a):
#             c=('{}{}{}'.format(i,j,q))
#             print(list((c))
# a='123456'
# i=(int)
# while True:
#     if str(i)==a:
#         print(i)
#         break
#     else:
#         i+=1
# A={1,2,3,4,5,6}
# B={1,2,3,7,8}
# c=A.union(B)
# print(c)
# 导入随机数库 【内置库】
# import random
# b=random.randint(1,10)
# print(b)
# 列表推导式
#print ([a for a in range (10)])
# 先写一个空的列表
# 定义一个新的变量名
# 写循环语句
# print([a for a in range (100) if a%2==0]) #100以内被2整除的数字
# 一张纸，厚度0.08mm，珠穆朗玛峰高8848m，求折叠多少次能超过珠穆朗玛峰？
# a = ["ads", "dafdsa5"," jjajs", "dfdsdas"]
# p = ["fdsfd", "fdsfdsaffdsa", "", "jjja", '213232'']

"""
账号长度在6～8之间为合法的账号
密码的长度在5～7之间为合法的密码
账号和密码都符合上述要求，将账号密码以键值对的形式保存
"""
# c=[]
# b=[]
# for i in a:
#     if len(i)>=6 and 8>=len(i):
#         c.append(i)
#         for j in p:
#             if len (j)>=5 and 7>=len(j):
#               b.append(j)
# print(dict(zip(c,b)))
# d={
#     "key":1000,
#     "key1":['我是列表'],
#     "key3":{1:2000,3:["a","b","c"]}
#     }

# k={1:10000,2:20000 }
# # k.setdefault("3")
# print(tuple(k))
import xlwt
a = [
    ["序号", "名字", "年龄", "性别"],
    [1, "张三", 20, "男"],
    [2, "李四", 19, "男"],
    [3, "王五", 18, "女"],
    [4, "赵信", 16, 	"女"]
    ]
#新建一个Excel文件
#第一步：新建一个Excel文件
#xlwt.workbook()新建一个文件excel文件
d =xlwt.Workbook()
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