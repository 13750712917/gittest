#/usr/bin/python
#-*-coding:utf-8-*-
#冒泡法排序
# a=[1,3,2,4,6,9,7,5]
# b=len(a)
# for i in range (b):
#     for j in range (b-1):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)
#选择法排序
# a=[1,3,2,5,4,9,6]
# b=len(a)
# for i in range (b):
#     for j in range (i+1,b):
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)
# #质数之和
# d=0
# for i in range (2,100):
#     for j in range (2,100):
#         b=i%j
#         if b==0:
#             break
#     if i==j:
#             d=d+i
# print(d)
# #水仙花数
# for i in range(100,1000):
#     b=i//100
#     c=i//10%10
#     d=i%10
#     if i==b**3+c**3+d**3:
#         print(i)
#阶乘之和
# a=int(input('请输入一个正整数：'))
# b=0
# for i in range (1,a+1):
#     c=1
#     for j in range (1,i+1):
#         c=j*c
#         b=b+c
#         print(b)

