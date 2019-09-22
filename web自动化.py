from selenium import webdriver#导入selenium中的webdriver模块
from time import sleep
import warnings
warnings.filterwarnings('ignore')
dr = webdriver.Chrome()#打开浏览器

# dr.set_window_size(1000, 1000)
dr.get('http://www.ifeng.com')#在URL中输入地址并请求

dr.find_element_by_xpath('/html/body/div[1]/div/div[3]/ul/li[1]/a').click()
sleep(3)
a=dr.window_handles
print(a)
dr.switch_to.window(a[1])
dr.close()

sleep(5)
dr.quit()

# print(dr.title)#title获取网页标题

# assert dr.title == '腾讯首页'# 断言：将实际结果与预期结果作对比
# dr.set_window_size(1000,1000)#窗口大小
# dr.maximize_window()#页面最大化
# dr.set_window_position(0,0)#设置窗口的位置
# print(dr.current_url)#获取网址
# sleep(3)
# dr.get('https://www.baidu.com/')
# sleep(3)
# dr.back()#af返回上一个网页
# sleep(3)
# dr.forward()#继续下一个网页

# time.sleep(2)
# dr.minimize_window()#页面最小化

#selenium核心——定位
#定位方法1 ID
# dr.find_element_by_id('kw').send_keys('python')
# sleep(3)
# dr.find_element_by_id('su').click()

#定位方法2 class
# dr.find_element_by_class_name('s_ipt').send_keys('python')
# sleep(3)
# dr.find_element_by_class_name('bg s_btn').click()

#定位方法3 name
# dr.find_element_by_name('wd').send_keys('python')
# sleep(3)
# dr.find_element_by_id('su').click()

#定位方法4 link_text文本定位
# sleep(3)
# dr.find_element_by_link_text('新闻').click()

#定位方法5 partial_link_text模糊文本
# time.sleep(3)
# dr.find_element_by_partial_link_text('hao').click()

# tag_name标签定位，不是唯一的，
# dr.find_element_by_tag_name('')

#xpath 路径定位，路径标记语言

#css_celector#层叠样式表
# dr.find_element_by_css_selector('#kw').send_keys('python')
# sleep(3)
# dr.find_element_by_id('su').click()


# dr.switch_to.frame('login_frame')#frame，内嵌框架，作用是切换框架，只能是ID或name的值，如果没有ID和name，就要先定位到该框架，再切换
# dr.switch_to.frame('login_frame')
# 退出框架
# dr.switch_to.parent_frame()#退回到上一层框架
# dr.switch_to.default_content()#退出到最开始的框架

'''
time.sleep(5)
# dr.find_element_by_id('switchAccountLogin').click()
# time.sleep(1)
dr.find_element_by_id('auto-id-1566359155535').send_keys('13750712917')
time.sleep(1)
dr.find_element_by_id('auto-id-1566359155538').send_keys('qwer1234tyuiop')
time.sleep(1)
dr.find_element_by_class_name('dologin').click()
# time.sleep(5)
# dr.quit()
'''


#定位一组元素:一次性定位到多个某些相同的元素
# dr.find_elements_by_class_name('')#与单个元素相比，element后边多了s

#层级定位：先定义大范围，再在大范围内定位元素
# a=dr.find_element_by_id('searchHotelLevelSelect').find_elements_by_tag_name('option')
# for i in a:
#     i.click()
#     time.sleep(2)
# dr.quit()

# time.sleep(5)
# a=dr.find_elements_by_class_name('cate_menu_lk')
# time.sleep(2)
# for i in a:
#     print(i.text)
#     time.sleep(2)

# dr.find_element_by_id('key').send_keys('微星GL')
# time.sleep(1)
# dr.find_element_by_class_name('button').click()
# dr.back()
# dr.find_element_by_
#current_window_handle 获取当前窗口的句柄
#window_handles 获取所有的句柄
# print(dr.current_window_handle)
#switch_to_window切换窗口