#/usr/bin/python
#-*-coding:utf-8-*-
f = open(file='a.txt', encoding='utf-8')
c=[]
k = f.readlines()
for i in k:
    a=i.replace(';', '').replace('\n', '').replace("'",'').replace('(','').replace(')','')
    b=a.split(',')
    c.append(b)
c.pop(len(c)-1)
for i in c:
    i.pop(len(i)-1)
    print(tuple(i))



# print(b)
# print()
# q.pop(-1)
# print(c)