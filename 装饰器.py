#装饰器：函数的一种包装，把函数A作为函数B中的一个参数，类似于函数的嵌套
'''
装饰器的本质就是函数，利用函数的返回值实现装饰器与被装饰函数之间数据的传递
函数不写return 依旧会返回一个None，return None与没有返回值效果是一样的。
'''
# def foo():
#     print('这是？？？')
#
#
# def koo():
#     print('啊哈哈哈')
#     foo()
#
# koo()

# def wa(func):
#     print('开始执行函数')
#     def inner():
#         print('开始执行inner函数')
#         func()
#         print('执行inner函数结束')
#     print('执行wa函数结束')
#     return inner
# def say():
#     print('say函数运行了')
#
# wa(say)()
'''
执行步骤
1、定义wa函数
2、定义say函数
3、执行wa(say) ---> 执行wa函数
4、进入wa函数内部，打印第一个print，定义inner函数，将inner函数返回给wa(say) ---> wa(say)=inner
5、wa(say)() ---> inner()
6、执行inner函数，打印第一个print,func() ---> say();执行say函数，将say函数的返回值返回给func(),打印第二个print，将inner函数的返回值返回给了wa(sya)()
7、程序退出
'''

def wa(func):
    print('开始执行函数')
    def inner():
        print('开始执行inner函数')
        func()
        print('执行inner函数结束')
    print('执行wa函数结束')
    return inner
@wa#@wa等价于wa(say)
def say():
    print('say函数运行了')

say()
'''
1、定义wa函数
2、执行@wa，执行wa函数，先打印print，定义inner函数，将inner函数返回给@wa
3、执行say()，相当于inner()函数，先打印print函数，再通过@wa定义并执行say函数，将函数的结果返回给func()，打印最后一个print，将inner函数的结果返回给say()
4、程序退出
'''

'''
@ 在Python中被称为语法糖
@+函数名 ---> 装饰器
@下的函数在执行时会自动创建并调用
'''