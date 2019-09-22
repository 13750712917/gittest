#/usr/bin/python
#-*-coding:utf-8-*-
#python 时间模块 time datetime 操作的时间、日期
import time
#sleep (浮点数/整数)
print('睡眠之前')
time.sleep(0.5)
print("睡眠之后")
#clock()计算的是执行代码时CPU花费的时间
# print(time.clock())
#ctime() asctime()获取当前时间
print(time.ctime())
print(time.asctime())
#输出时间的详细信息  localtime() 本地时区
print(time.localtime())
#格式化输出时间 strftime("关于时间的字符串")
print(time.strftime("%A  %B %H: %M: %S"))
"""
%a   本地化的缩写星期中每日的名称。
%A   本地化的星期中每日的完整名称。
%b   本地化的月缩写名称。
%B   本地化的月完整名称。
%c   本地化的适当日期和时间表示。
%d   十进制数 [01,31] 表示的月中日。
%H   十进制数 [00,23] 表示的小时（24小时制）。
%I   十进制数 [01,12] 表示的小时（12小时制）。
%j   十进制数 [001,366] 表示的年中日。
%m   十进制数 [01,12] 表示的月。
%M   十进制数 [00,59] 表示的分钟。
%p   本地化的 AM 或 PM 。
%S   十进制数 [00,61] 表示的秒。
%U   十进制数 [00,53] 表示的一年中的周数（星期日作为一周的第一天）作为。在第一个星期日之前的新年中的所有日子都被认为是在第0周。
%w   十进制数 [0(星期日),6] 表示的周中日。
%W   十进制数 [00,53] 表示的一年中的周数（星期一作为一周的第一天）作为。在第一个星期一之前的新年中的所有日子被认为是在第0周。
%x   本地化的适当日期表示。
%X   本地化的适当时间表示。
%y   十进制数 [00,99] 表示的没有世纪的年份。
%Y   十进制数表示的带世纪的年份。
%z   时区偏移以格式 +HHMM 或 -HHMM 形式的 UTC/GMT 的正或负时差指示，其中H表示十进制小时数字，M表示小数分钟数字 [-23:59, +23:59] 。
%Z   时区名称（如果不存在时区，则不包含字符）。
%%   字面的 '%' 字符。
	
"""
#strptime("关于时间的字符串")  %y 表示年份 %d 表示一个月第几天  %b 表示的是月份
print(time.strptime("30 Dec 01","%d %b %y"))
#计算计算机元年到现在所有秒的总和   time()
 print(time.time())


#python 对日期的操作
#datetime
from datetime  import datetime,date,timedelta #精确导入
#import datetime  整体导入
#1、获取当前时间、日期  datetime.now()
print(datetime.now())
#2、获取指定的时间、日期 datetime（数字【整数】）
print(datetime(2019,7,30,9,51,1))
#3、将时间字符串：转成datetime里的日期 2019-07-30 09:51:01   strptime()
k = datetime.strptime('1937-7-7 12:00:00','%Y-%m-%d %H:%M:%S')
print(k)
#4、将日期装换为字符串 strftime()
print(datetime.now().strftime("%H:%M:%S"))

#5、日期的加减
#求当前时间
a = datetime.now()
print(a)
#加3个小时 hours=3   3天 days =3 3秒 seconds =3
b = a + timedelta(hours =3)
print(b)
#6、获取当前的日期 today() --->2019-07-30
print(date.today())
#对日期进行加减
#步骤一、获取当前的日期
#步骤二、加减日期 timedelta(days=xxx)
f = date.today()+timedelta(days=2)
print(f)