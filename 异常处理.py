#处理异常try ... except
'''
异常
1.语法错误，缩进，缺少符号
2.逻辑错误
'''

#异常处理，针对Python代码中可能出现的错误或异常进行处理
# try:
#     # a=1/0
#     # print(a)
#     print(name)
#     print('成功')
# except (ZeroDivisionError , NameError):
#     print('try语句有错误')

#try ... except ... finally
# try :
#     a=1/0
# except:
#     print('try语句有bug')
# finally:
#     print('fially语句被执行了')
# try:
#     a=1/0
# except:
#     print('ksc')
# else:
#     print('KNSC')

#flask：web框架,python 开发web网页，数据交互的一个web框架
'''
django
flask
bottle
tormdon

web页面一般分两种
1、静态的   页面不会发生变动
2、动态的   页面的数据实时刷新
'''
flask
from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello():
    return 'hello falsk'
if __name__=='__main__':
    app.run(host='127.0.0.1',port=6000)


