#/usr/bin/python
#-*-coding:utf-8-*-
# #河南大学类
# class Heda (object):
#     yuanxi="物理系"
#     canting="北苑餐厅"
#     chaoshi="三星超市"
#     caochang="志义体育场"
#     def print_yuanxi(self):
#         print(f"小王是{self.yuanxi}的学生")
#     def print_canting(self):
#         print(f"他经常去{self.canting}吃饭")
#     def print_chaoshi(self):
#         print(f"课间时他还会去{self.chaoshi}买零食吃")
#     def print_caochang(self):
#         print(f"每星期的周四他在{self.caochang}上体育课")
#a = Heda()
#a.print_yuanxi()
# a.print_canting()
# a.print_chaoshi()
# a.print_caochang()
#狗类
# class dog (object):
#     goutui = '4'
#     def __init__(self,maose,shenggao,pinzhong,tizhong):
#         self.maose = maose
#         self.shenggao = shenggao
#         self.pinzhong = pinzhong
#         self.tizhong = tizhong
#     def print_goutui(self):
#         if self.goutui==4:
#             print('这是一只健全的狗')
#         else:
#             print("这是是一只残狗")
#     def print_maose(self):
#         print(f"狗的颜色是：{self.maose}")
#     def print_shenggao(self):
#         print(f"狗高{self.shenggao}")
#     def print_pingzhong(self):
#         print(f"这是一只{self.pinzhong}")
#     def print_tizhong(self):
#         print(f"狗的重量为：{self.tizhong}")
#     def eat(self):
#         if self.eat:
#             print("主人，我要吃食物")
#         else:
#             print("谢谢主人，我不饿")
#     def he(self):
#         if self.he:
#             print("主人，我要喝水")
#         else:
#             print("谢谢主人，我不渴")
#     def jiao(self):
#         if self.jiao:
#             print("遇见陌生人，旺旺")
#         else:
#             print("你是好狗")
#     def pao(self):
#          if self.pao:
#             print("挨打时就跑")
#          else:
#             print("傻狗")
# A  = dog('黄色',140,'藏獒','35kg')
# A.print_goutui()
# A.print_maose()
# A.print_shenggao()
# A.print_pingzhong()
# A.print_tizhong()
# A.pao()
# A.eat()
# A.he()
# A.jiao()
# class Dog (object):
#     dog_leg= 4
#     def __int__(self,pingzhong,maose,shenggao,tizhong):
#         self.pingzhong=pingzhong
#         self.maose=maose
#         self.shenggao=shenggao
#         self.tizhong=tizhong
#     def eat (sellf):
#         print("这只狗饿了会吃")
#     def  drink(self):
#         print("了渴会水")
#     def pao(self):
#         print("这只狗挨打了会跑")
#     def jiao(self):
#         print(f"隔壁老王家有一只品种是{self.pingzhong},毛的颜色为{self.maose},体重为{self.tizhong},身高为{self.shenggao}的{self.dog_leg}狗，")
# A= Dog('cdasasd','ada','adsa','adsdas')
# A.eat()
# A.pao()
# A.jiao()
# A.drink()

# class Book(object):
#     str_book={'001':'时间简史','002':'水浒传','003':'红楼梦','004':'西游记','005':'三国演义'}
#     def show(self):
#         print(f'图书编号{self.str_book.keys}\t\t书名{self.str_book.values}\t\t')
#     def cha(self):
#         while True:
#             a=input("请输入图书名字：")
#             for i in self.str_book.values():
#                 if a in self.str_book:
#                     print()
#
# A=Book()
# print(A.show())
# class Book (object):
#     books=[ ['西游记',  '吴承恩','1','A1'],
#             ['红楼梦',  '曹雪芹','1','B2'],
#             ['水浒传',  '罗贯中','1','C5'],
#                ['三国演义','施耐庵','1','D3']
#             ]
#     def __init__(self,bookname,zuozhe,zhuangtai,weizhi):
#         self.bookname = bookname
#         self.zuozhe = zuozhe
#         self.zhuangtai =zhuangtai
#         self.weizhi =weizhi
#     def  showbook(self):
#         # a=self.books
#         print(f"\t\t\t\t\t\t\t\t图书管理系统")
#         print(f"\t\t书籍编号\t\t\t书名\t\t\t作者\t\t\t状态\t\t\t区域")
#         for i ,j  in enumerate(self.books):
#             print(f"\t\t\t{i}\t\t\t\t{j[0]}\t\t\t{j[1]}\t\t\t{j[2]}\t\t\t\t{j[3]}")
# a=Book(1,2,3,4)
# a.showbook()
class Xinxi(object):
    f = open(file='a.txt', encoding='utf-8')
    a=[]
    k=(f.read())
    l = k.replace("(", '').replace(';', '').replace('\n', '').split(')')
    for i in l:
        a.append(i.replace("'",'').split(','))
    def  jianbiao(self):
        import pymysql
        d = pymysql.connect(
            host='192.168.10.60',
            port=3306,
            user="root",
            password="123456",
            charset="utf8",
            database="hao123",
        )
        e = d.cursor()
        sql1 = "create table xinxi (公司 char(20),职位 char(20), 网址 char(50), 公司类型 char(30), 是否上市 char(20),规模 char(20),地址 char(30), 工作经验 char(20), 学历 char(10))"
        self.e.excute(sql1)
        sql2 ="insert into xinxi values (self.xieru)"
        self.e.execute(sql2)
        self.d.commit()
k=Xinxi()
k.xieru()
           
            











