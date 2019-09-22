#/usr/bin/python
#-*-coding:utf-8-*-
#print( 'hello')
#变量
#a='WANGFENGTAO'
#b=a.swapcase()
#print (b)
#print(b.swapcase())
#c='wang'.title()+'feng'.title()+'tao'.title()
#print (c)
#a='hellodhello'
#print (a.endswith ("o"))
#a='-'.join('67891')
#print(a)
#print(a.upper())
#a='{}hello{}'
#b='nihao'
#c=a.format(b,'you')
#print(c)
#b=' adadda'
#print(b)
#b=' adadda'
#d=b.strip()
#print(d)
#a=['121','wqw','111','4332','111,''qwer',[1,2,3],'hello,python']
#a.append('qwe')
#print(a)
#a.insert(3,'hello,python')
#a.remove('111')
#print(a)
#a.pop(1)
#print(a)
#a.sort()
#print(a)
#a.reverse()
#print(a)
#a.reverse()
#print(a)
#b=['wang','feng','tao']
#b=a.copy()
#a[5].append(3)
#print(b)
#c=copy.deepcopy(a)
#a[5].append(3)
#print(c)
#a='%s是第%d本书'%('这',1)
#print (a)
#a='{}hello{}'
#print(a.format('ni','python'))
#a=[121,212,323,12,23,12]
#print(a.count(12)
#a.sort()
#print(a)
#a.reverse()
#print(a)
#a={'wqe','1213','qscw','qaz','1213','wqe'}
#a.add(12)
#print(a)
#a.pop()
#print(a)
#a={'姓名':'wang','性别':'man','so':'hao'}
#b={'age':21}
#a.update(b)#必须是同一个数据类型
#print(a)
#a=(12,12,22,11,)
#b=set(a)
#print(b)
#a=hex(192)
#print(a)
#a=oct(192)
#print(a)
#a=bin(192)
#print(a)
#a=int(0x11111)
#print(a)
#a=ord('1')#字符需要加引号，否则会报错
#print(a)
#a=chr(97)
#print(a)
#a=[1 ,2,22]
#b=sum(a)
#print(b)
#a,b=divmod(15,4)
#print(a)
#print(b)
#a='lianajie'
#b=a.split('a')
#c='_'.join
#print(c)
#a='{} love {}'
#b='I'
#c=a.format(b,'you')
#print(c)
#a='  aqwe  '
#print(a)
#b=a.strip()
#print(b)
#b=a.lstrip()
#print(b)
#b=a.rstrip()
#print(b)
#s="""Then one day the mother eagle appeared at the top of the mountain cliff, with a big bowl of delicious food and she looked down at her baby. The baby looked up at the mother and cried "Why did you abandon me? I'm going to die any minute.'How could you do this to me?"""
#c=s.split(',')
#print(c)
#a={'name':'wangfengtao','age':'22' }
#a.popitem()
#print(a)
#text = "Early in the day it was whispered that we should sail in a boat, only thou and I, and never a soul in the world would know of this our pilgrimage to no country and to no end"
#g=text.split('')
#print(g)
#求国家个数
# 求所有学生的身高范围
# 求统计男女比例
# 求平均身高
# 查询身高在170到180之间的学生名字




d = {
    "data": {
        "msg":
        [
            {
                "s_1": ["Jim", "男",  19, "175cm"],
                "country": "美国"
            },
            {
                "s_2": ["Kity", "女",  17, "165cm"],
                "country": "法国"
            },
            {
                "s_3": ["Tom", "男",  19, "173cm"],
                "country": "美国"
            },
            {
                "s_4": ["拖拉斯基", "男",  18, "180cm"],
                "country": "俄罗斯"
            },
            {
                "s_5": ["阿卡丽", "女",  17, "175cm"],
                "country": "乌克兰"
            },
            {
                "s_6": ["牙买稻子", "女",  18, "161cm"],
                "country": "日本"
            },
            {
                "s_7": ["龟田一郎", "男",  19, "175cm"],
                "country": "日本"
            },
            {
                "s_8": ["张三", "男",  20, "180cm"],
                "country": "中国"
            },
            {
                "s_9": ["李秀琴", "女",  19, "175cm"],
                "country": "中国"
            },
            {
                "s_10": ["宋仲基", "女",  19, "175cm"],
                "country": "韩国"
            },
            {
                "s_11": ["金正鞋", "男",  19, "168cm"],
                "country": "朝鲜"
            },
            {
                "s_12": ["卡列夫斯基", "男",  21, "190cm"],
                "country": "俄罗斯"
            },
        ]
    },
}
d1=d['data']['msg']
n=[]
s=[]
a=[]
h=[]
c=[]
for i in d1:
    for j in i.values():
        if type(j)==list :
            n.append(j[0])
            s.append(j[1])
            a.append(j[2])
            h.append(j[3])
        else:
            c.append(j)
# e=set(c)
# x=int()
q=0
for w in h:
    q=q+int(w.replace('cm',' '))
print("平均身高：{}".format(q/len(h)))

# print("国家个数:{}".format(len (e)))
# print( "身高范围：{}— {}".format(max(h),(min(h))))
# print("男女身高比例：{}".format(s.count("男")/s.count("女")))
# x=' '.join(h)
# k=x.replace("cm"," ")
# int(k)
# print(k)




# 冒泡循环
# a=[3,1,4,5,2]
# b=len(a)
# for i in range (b ):
#     for j in range (b-1):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)
# a=["面包","火腿","香蕉","苹果","桔子"]
# b=[30,50,20,25,40]
# k=[90,35,20,70,26]
# print('商品编号\t商品名\t\t\t单价')
# for i ,j in enumerate(a):
#     print('{}\t\t\t{}\t\t\t{}'.format(i,j,b[i]))
# h=(input('是否购买:y/q'))
# if h=='y':
#     c= int(input('请输入编号'))
#     d= int(input('请输入购买数量'))
#     zhangdan=b[c]*d
#     print(f'你购买的商品:{a[c]},购买的数量:{d},消费金额:{zhangdan}')
#     e=(input('您是否使用会员:yes/no '))
#     if e=='yes':
#         g=(input('请输入会员卡号: '))
#         v=(input('请输入密码：'))
#         if g in ['123456']:
#             print()
#         if v in ['12345']:
#             print('应付金额{}'.format(zhangdan*0.95))
#         else:
#             print('会员卡号输入错误')
#     elif e=='no':
#         print('应付金额{}'.format(zhangdan))
# if h=='q':
#             print('欢迎下次再来')













