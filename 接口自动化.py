#！usr/bin/python
#-*-coding:utf-8-*-
#接口测试：验证url是否能够正常请求和响应的过程
import requests
import json
"""
json.loads的作用是将json字符串转化成字典
a='{"Sncs":"gbadv","asdgads":"dgasd"}'
b=json.loads(a)
print(b)

json.dumps将字典转换成json字符串
a={"Sncs":"gbadv","asdgads":"dgasd"}
b=json.dumps(a)
print(b)
"""
class Dian_ma_zhuan_huan():
    url1='http://v.juhe.cn/cccn/to_telecodes.php'
    url2="http://v.juhe.cn/cccn/to_chinese.php"
    head={
        'User - Agent':'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 70.0.3538.102Safari / 537.36Edge / 18.18362'
    }

    def test_1(self):
        canshu={'key':'74cdd42dfe76706b6aff2902cfcd848b','chars':'鱼香肉丝'}
        res=requests.get(url=self.url1,headers=self.head,params=canshu)
        html = res.json()
        assert html["reason"] == 'success'
        print('断言成功!')

    def test_2(self):
        canshu={'key':'74cdd42dfe76706b6aff2902cfcd848b','telecodes':'2207'}
        res = requests.get(url=self.url2, headers=self.head, params=canshu)
        html = res.json()
        assert html["reason"] == 'success'
        print("断言成功!")
a=Dian_ma_zhuan_huan()
a.test_1()
a.test_2()