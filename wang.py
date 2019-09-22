#/usr/bin/python
#-*-coding:utf-8-*-
# print("这是abc里的代码")
#
# if __name__ == '__main__':
# # __name__代表当前文件的名字
# # __main__代表当前文件的名字
#
# #python程序入口，只能在当前文件下执行 if __name__ == '__main__':
# #低下的代码，离开这个文件， if __name__ == '__main__':条件不成立了
#
#     print("这是if语句下的代码")

while True:
    a = int(input('请输入第一条边长:'))
    b = int(input('请输入第二条边长:'))
    c = int(input('请输入第三条边长:'))
    if a+b>c and a+c>b and b+c>a:
        if a==b and b==c and a==c:
            print('这是一个等边三角形')
        elif a==b or a==c or b==c:
            print('这是一个等腰三角形')
        else:
            print('这是一个不规则三角形')
    else:
        print('这不是三角形')