#/usr/bin/python
#-*-coding:utf-8-*-
#无参数，无返回值
#组织函数代码
# def add():
#     n=0
#     for i in range(101):
#         n+=i
#         print(n)
# add()
       #函数的使用
"""
第一步：先写函数的名字
第二步：（），如果里面有参数，则传入值
"""
# 有参数无返回值
#  x  c参数类型属于必填参数，使用函数的时候就必须传入值
# def add(x):
# #     n=0
# #     for i in range(x):
# #         n+=i
# #         print(n)
# # add()
#全局变量
"""
全局变量定义之后，在整个脚本的所有行都可以使用
"""
#局部变量
"""
局部变量定义之后，只能在特定的范围使用
"""
#有参数，有返回值
# def add(x):
#     n=0
#     for i in range(x):
#         n+=i
#         print(n)
#         return n  #函数没有返回值是没有意义,当一个函数没有返回值的时候，它标识着空（None），print输出结果为（None）
# print('dqwdqd')
# print(add(3))#直接打印函数名---结果是函数在内存的位置
#return的作用？
# 1、返回值
# 2、标识一个函数的结束
# a=1000#全局变量
# def cha(x1,x2):
#     #局部变量
#     b=10000
#     chazhi=b-x1-x2
#     return chazhi
# print(cha(100,10))
#函数质数之和
# def fun(a):
#     d=0
#     for i in range (2,a):
#         for j in range(2,i+1):
#             b=i%j
#             if b==0:
#                 break
#         if i==j:
#             d+=i
#     print(d)
#     return fun
# fun(100)






#参数类型第二种，默认参数 y =100 y 后面的就是默认值
#在函数使用的时候，如果不对默认参数进行赋值，那么就使用默认值
# def f (x, y=100):
#     print(x+y)
# f(10)
#参数类型第三种，可变长参数 *args  **kwargs
#*args
"""
1、传入多个值
2、args是元组的形式
3、传入的多个值被转换为一个元组
"""
# def d (*args):
#     a,b,c=args
#     print(a)
#     print(b)
#     print(c)
#     print(args)
# d([1,],[2,],[3,])
## **kwargs,可变长参数 **kwargs
"""
1、传入值的时候有以类似于字典的形式(a1=2,a2=3，a3=4)
2、kwargs是字典，可以使用字典的 所有函数
3、z,x,c=kwargs.values()
"""
# def  j(**kwargs):
#     print(kwargs)
#     z,x,c=kwargs.values()#获取kwargs中传入的所有值
#     print(z)
#     print(x)
#     print(c)
# j(a1=2,a2=3,a3=4)
#q=int(input('输入数字: '))
# def d (*args):
# #     a=len(args)
# #     if a==0:
# #         print('请给参数赋值,输入2个或4个数字，以英文逗号隔开')
# #     elif a==2:
# #        m=max(args)
#          n=min(args)
# #             a=0
#               c=1
# #             for i in range (n,m+1):
# #                     c=c*i
# #                 a+=c
#      print
# #     elif a==4:
# #         i=[]
# #         for q in (1,5):
# #             for w in (1,5):
# #                 for e in (1,5):
# #                     for r in (1,5):
# #                         if(q!=w)and(w!=e)and(e!=r)and (r!=q):
# #                             i+=1
# #                             print ('共{}种组合'.format(i))
# #     else:
# #         print('该函数不执行')
# # d()
# # print(d(1,2,3,4))


# def j (**kwargs):
#     if z==str:
#     z,y=kwargs.items()
#     print(z)
#     print(y)
# j(a=1,s=1)
# for i in kwargs.values():
#         if type(i)==tuple:
#             yz.append(i)
#             if len(yz)>3:
#                 break
#         elif type(i)==list:
#             list_1.append(i)
#             if len(list_1)>3:
#                 break
#         elif  type(i)==str:
#             str_1.append(i)
#             if len(str_1)>3:
#                 break
#         elif type==dict:
#             dict_1.append(i)
#             if len(dict_1)>3:
#                 break
#         elif type(i)==int:
#             int_1.append(i)
#             if len(int_1)>3:
#                 break
#         else:
#             jih.append(i)
#             if len(jih)>3:
#                 break
#     print('字符串元素有', len(str_1), '个')
#     print('元组元素有', len(yz), '个')
#     print('数值元素有', len(int_1), '个')
#     print('字典元素有', len(dict_1), '个')
#     print('列表元素有', len(list_1), '个')
#     print('集合元素有', len(jih), '个')
#     print(str_1)
#     print(yz)
#     print(int_1)
#     print(dict_1)
#     print(list_1)
#     print(jih)
#
# zd(a1=1,a2=2)
# def k (q,y=[1,2,3,4,5,6,7,8,9]):
#     if q in y:
#         w=y. index(x)
#         for i in range(w):
#             y.append (y[0])
#             x.pop(0)
#         return(y)
#     else:
#第四道
# q={}
# def k (y,*args):
#     t=y+sum(args)
#     return(t)
# def w (z):
#     return(z)
# i=k(12,2,3)
# j = w(['a','b',1])
# b=q.fromkeys(j,i)
# print(b)
#第五道
# import random
# d = {'admin':'12345','abc':'123','user':'54321'}
# def session(x,y):
#     A = ''
#     for i,c in d.items():
#         if x == i and d[i] == y:
#             A = x + y
#             while True:
#                 if len(A) >= 8:
#                     a = random.randint(6,8)
#                     b = ''
#                     for j in range(a):
#                         q = random.choice(A)
#                         b += q
#                     return f'这是session：{b}'
#                 else:
#                     e = random.randint(0,9)
#                     f = str(e)
#                     A += f
#     else:
#         return '请重新输入用户名和密码'
#
# print(session('admin','12345'))
# print(session('abc','123'))
# print(session('admin',2))

#函数嵌套
# def k ():
#     print("k函数的代码")
#
#
# def f (a):
#     a()
# f(k)
#python读写txt文本，对文件的操作
#f=open(file='a.txt',encoding='utf-8')
# print(f.read())           #read()读取全部
# print (f.readlines())#读取出来的数据以列表的形式保存
"""
file:指的的是文件的名字、或者说文件在计算机中存放的路径【必填参数】
mode：‘r’表示读取，‘w’表示写入，会自动创建一个文件，【文件不存在的时候】
‘x’创建文件并写入数据到文件里。会自动创建一个文件，‘a’向文件里添加数据‘b’二进制的形式
‘rb’应用于读取文件、mp3.mp4、
‘wb’应用于写入照片、mp3，mp4、
"""
# f=open(file='a.txt',mode='a',encoding='utf-8')
# f.write('\nhello,python')
#打开照片
# f=open(file=r'‪C:\Users\123456\Desktop\QQ图片20190720170725.jpg',mode='rb')
# #保存照片
# f=open(file='hello.jpg',mode='wb')
# d.write(f.read())
#写两个函数，函数一：读取电脑中的任意位置的txt文件，读取文件里的所有内容
#函数二：向txt中可以追加写入数据，保存文件位置由使用者自行决定
# def rb():
#      f= open(file='txt', encoding='utf-8')
#      print(f.read())
# def wb(k):
#      k()
#      f = open(file='txt', mode='a', encoding='utf-8')
#      f.write('\nhello,python')
# wb(rb)
# f = open(file=r'C:\\Users\123456\Desktop\20190720170725.jpg', mode='rb')   #打开照片
# d = open(file='kkk.jpg', mode='wb')     #保存照片
# d.write(f.read())

#匿名函数
"""
lambda 参数： 代码块
代码块只能写一行，不能中断
不支持循环，不支持判断
"""

# def a(x):
#     print(x+1)
# a(2)
# f = lambda x: x+1
# f(2)
#
# f = lambda k,y: k-y
# print(f(100,10))



