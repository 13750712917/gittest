#/usr/bin/python
#-*-coding:utf-8-*-
"""
class 类名（）：
     #类的代码
     #代码包括，循环、判断、函数
"""
#定义一个动物园的类
class  zoo(object):      #object括号里指的是继承于哪一个类
    #属性
    dongwu = "老虎"
    #方法
    def biaoyan(self):       #self等于对象本身
        print(f"有一个神奇的动物,{self.dongwu}在表演！")


"""
object #翻译成中文叫做对象   
object;所有类的基类       
self :在方法里面第一个参数是self；
self指代的是对象的本身
对象可以使用类的属性和类的方法
"""
#类的使用
#第一步，创建对象
# a = zoo()   #a对象
#第二步，使用对象操作类的属性、方法。
# print(a.dongwu)
# a.biaoyan()
"""
1、属性：
       # 从公有私有的角度？
       公有的属性
       私有的属性
       #从类、对象的角度？
       类属性
       对象属性 == (实例属性)
2、方法     
"""
#学生类
#类的属性
class Student(object):
    类的属性
    # name = "渣男"
    # grade = "1903"
    # sex = "True"  #男生：True，女生：False

    book = ['言情系列','都市系列','玄幻系列']
    #初始化方法
    def __init__(self,name,grade,sex):
        #对象的属性
        self.name = name
        self.grade = grade
        self.sex =sex
    # 打印名字的方法
    def print_name(self):
        print(f"有个学生的名字叫做{self.name}")
    #打印学生的班级
    def print_grade(self):
        print(f"有个学生叫{self.name}，在{self.grade}班级里，他python学的贼好")
    #打印学生的性别
    def print_sex(self):
        if self.sex:
            print("哇！靓仔！！！")
        else:
            print("哇！靓女！！！")
 #打印学生书包里的图书
    def print_book(self):
        for i in self .book:
            print(f"书包里的书有：{i}")
#类可不可以使用对象的属性？
"""
类不能使用对象的属性
类名 ————  代表类
2、类可以访问类的属性
"""
#对象可不可以使用对象属性、类属性？
"""
1、对象可以访问对象属性
2、对象可以访问类属性
"""
# A=Student("张三",12,True)
# print(A.book)

 
# #使用类的代码
A = Student("王五",123,True)
A.print_name()
A.print_grade()
A.print_sex()
# #def __init__(self):
# B = Student("李四",1232,False)
# B.print_name()
# B.print_grade()
# B.print_sex()
#老师类
class Teacher(object):
    #类属性：公有 私有
    #公有属性
    ke = ['语文','数学','外语','生物']
    #私有属性标志，双英文的下划线开头
    __grade = '1903'
    a = 'as'
#初始化方法、【魔法放法】
    def __init__(self,a,b):
        #对象属性
        #公有的对象属性
        self.a =a
        #私有的对象属性
        self.__b=b
        self.c='hello'
#实例方法
    def kl(self):
        print(f"方法访问类的公有属性：{self.ke}")
        print(f"方法访问类的私有属性：{self.__grade}")
#实例方法
    def g (self):
        print(f"方法访问类的公有属性：{self.a}")
        print(f"方法访问类的私有属性：{self.__b}")
#私有方法
    def __w(self):
        print("这是一个私有方法")
    #在类的外部通过对象 . 方法名来访问方法，在类的内部，self.方法名来访问方法
    #self 等价于一个 对象，访问方法、属性通过对象来操作的
   #实例方法
    def h(self):
        self.__w()
 #@在python里被称为语法糖
    @classmethod            #装饰器：将一个实例方法变成类方法。
    def  bowen(cls):
        print("这是一个类方法")
    @staticmethod   #装饰器：将一个实例方法变成类方法。
    def python():  #像一个没有参数的函数
        print("这是一个静态方法")


"""
@classmethod            #装饰器：将一个实例方法变成类方法。
私有属性定义的原因？
属性一旦被定义，不希望被更改
"""

print(Teacher.ke)
#更改类属性对象的值
Teacher.ke = (1,2,3)
print(Teacher.ke)
#更改对象属性，只能通过对象来修改它
t3 = Teacher(1,2)
#更改之前的
# print(t3.c)
t3.c = 'python'
#私有的不能在外面用
# t3.__w()
#更改之后的
print(t3.c)
t3.h()
"""
类方法：参数cls
cls self 都是指向对象本身
cls作为参数的方法可以通过类名.方法来访问
"""
# t4 = Teacher('122',2)
# print(t4.c)

#在类的外部，类、对象都不能访问类的私有属性
# print(Teacher.__grade)
#print(t1.__grade)
#  对象可以访问类的私有属性、类的公有属性【在类的内部】
# t1 = Teacher()
# t1.k1()
# print

# t2 = Teacher('你好','python')
#私有的对象属性不能通过对象在类的外部访问
# print(t2.__b)
#  对象可以访问类的私有属性、类的公有属性【在类的内部】
# t2.g()
#静态方法可以通过类名.静态方法、对象.静态方法名来访问
# Teacher.python()
# t3.python()
#方法：静态、类方法、实例 【普通方法】 、魔法方法
#私有方法


