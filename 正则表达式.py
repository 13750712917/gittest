#/usr/bin/python
#-*-coding:utf-8-*-
#python正则表达式  模块 re  正则模块 【只能操作字符串 】
import re
"""
1、 . 在python里表示除了换行符\n以外任意一个字符
2、 * 匹配*前面的字符0次或多次
3、 + 匹配+前面的字符1次或者多次
4、 ? 匹配？前面的字符0次或1次
5、 $ 以某个字符结尾
6、 ^ 以某个字符开头
7、{m}匹配{}前面字符m次
8、{m,n}匹配{}前面字符m-n次,最少m次、最多n次
9、[abc]匹配[] 里的任意一个字符
10、\d  [0-9]
11、\D  除了0-9以为的任意一个字符
12、\s表示空白字符串Unicode \t \n \r \f \v
13、\S表示除了空白字符以为任意一个字符
"""
#贪婪模式
"""
指的是尽可能的匹配更多的字符
"""
#非贪婪模式
"""
指的是匹配到符合规则的，就停止匹配
"""
#sub (参数1，参数2，参数3)替换的意思 str.replace('旧的'，'新的')
"""
参数1：正则
参数2：新的字符
参数3：被更改的字符串
"""
#group()组  作用：将我们匹配到的内容拿出来
#groups()多个分组

# URL ="https://www.baidu.com"
# r11 = re.compile(r'\.(.*)\.')
# q=re.search(r11,URL).group()
# # print(q)
# b=re.sub(r'\.','',q)
# print(b)
#贪婪模式
# URL ="https://www.baidu.comhttps://www.ifeng.com"
# r11 = re.compile(r'\.(.*)\.')
# q=re.search(r11,URL).group()
# print(q)
# b=re.sub(r'\.','',q)
# print(b)
#非贪婪模式 存在一个 ?
# URL ="https://www.baidu.comhttps://www.ifeng.com"
# r11 = re.compile(r'\.(.*?)\.')
# q=re.search(r11,URL).group()
# print(q)
# b=re.sub(r'\.','',q)
# print(b)

#findall() --->结果是列表，每个元素都是字符串
#作用：找出字符串中所有符合正则规则的结果
# URL ="https://www.baidu.comhttps://www.ifeng.com"
# r11 = re.compile(r'\.(.*?)\.')
# q=re.findall(r11,URL)
# print(q)
# s = '13212503827321315278912345'
#search(参数一，参数二):从左边开始搜索
"""
参数一：已经编译好的正则表达式
参数二：要匹配的字符串
"""
#写正则的步骤：
#第一步：编译正则表达式  re.compile(r'.')这个编译的过程，r1代表编译完成的正则表达式
# s = '123456'
# r1=re.compile(r'.')
# q=re.search(r1,s)
# print(q)
# s = '123456'
# r2=re.compile(r'3*')
# q=re.search(r2,s)
# print(q)
# s = '123456'
# r3=re.compile(r'3+')
# q=re.search(r3,s)
# print(q)
# s = '123456'
# r4=re.compile(r'1?')
# q=re.search(r4,s)
# print(q)
# s = '123456'
# r5=re.compile(r'6$')
# q=re.search(r5,s)
# print(q)
# s = '123456'
# r6=re.compile(r'^1')
# q=re.search(r6,s)
# print(q)
# s = '12223456'
# r7=re.compile(r'2{3}')
# q=re.search(r7,s)
# print(q)
# s = '12223456'
# r8=re.compile(r'1{1，2}')
# q=re.search(r8,s)
# print(q)
# s = '12223456'
# r9=re.compile(r'1[23]')
# q=re.search(r9,s)
# print(q)
#第二步：执行正则表达式
# q=re.search(r9,s)
# # print(q)
#过滤手机号
# r=re.compile(r'(135)[0-9]{8}|(152)[0-9]{8}')
# pritn(re.match(r,s))
# print(re.search(r,s))
#match与search的区别
"""
match:一旦匹配不到，立刻结束匹配
search：匹配继续匹配，直到匹配成功第一次或者字符串结束为止
#共同点
直到匹配成功第一次之后就停止
"""