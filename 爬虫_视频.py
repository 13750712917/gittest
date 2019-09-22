import re
import requests
a=requests.get(url='https://www.51miz.com/shipin/0-1-0-1.html?utm_term=1349533&utm_source=baidu')
b=a.content.decode(encoding='utf8')
# print(b)
r1=re.compile(r'280" src="(.*?).mp4"')
r2=re.compile(r'280" alt="(.*?)"')
c1=re.findall(r1,b)
c2=re.findall(r2,b)
for i in range(len(c1)):
    print(c1[i])
    # print(c2[i])