import requests,re
'''
a1=requests.get(url='http://www.doutula.com/article/detail/6162282')
b1=a1.content.decode(encoding='utf8')
# print(b1)
r=re.compile(r'<img referrerpolicy="no-referrer" src="(.*?)" alt="(.*?)"')
t=re.findall(r,b1)
# print(t)
for i in t:
    a2=requests.get(url=f'{i[0]}')
    jiegou = a2.content  # 图片 二进制
    f = open(file=f'e:/表情包/{i[1]}.gif', mode='wb')
    f.write(jiegou)
    print(f'{i[1]}.gif')
'''

for i in range(1,11):
    a1=requests.get(url='http://www.doutula.com/photo/list/?page='+f'{i}')
    b1=a1.content.decode(encoding='utf8')
    r=re.compile(r'data-original="(.*?)" alt="(.*?)"')
    t=re.findall(r,b1)
    # print(t)
    for j in t:
        a2=requests.get(url=f'{j[0]}')
        jiegou = a2.content  # 图片 二进制
        b1 = j[0][len(j[0]) - 1]
        b2 = j[0][len(j[0]) - 2]
        b3 = j[0][len(j[0]) - 3]
        c=b3+b2+b1
        f=open(file=r'e:/表情包/{j[1]}.{c}', mode='wb')
        f.write(jiegou)
        print(f'{j[1]}.{c}')