from selenium import webdriver
from time import sleep
import warnings
import selenium.webdriver.support.ui as ui#智能等待
from selenium.webdriver.common.action_chains import ActionChains
warnings.filterwarnings('ignore')
dr = webdriver.Chrome()#打开浏览器
dr.get('https://qzone.qq.com')
dr.maximize_window()#页面最大化

'''
#操作弹出框
sleep(2)
dr.find_element_by_xpath('/html/body/button').click()
sleep(2)
w=dr.switch_to_alert()#弹出框
sleep(2)
print(w.text)
w.send_keys('哈哈')
sleep(2)
w.accept()
'''
'''
#控制浏览器的滚动条

#根据元素滚动
dd=dr.find_element_by_xpath('//*[@id="J_app"]/div[6]/ul/li[1]/a/span[2]')
#arguments[0].scrollIntoView();     操作滚动条
dr.execute_script('arguments[0].scrollIntoView();',dd)#dd是页面中的某个元素

#根据距离滚动
for i in range(0,10000,200):
    js=f"var q=document.documentElement.scrollTop={i}"
    dr.execute_script(js)
    sleep(1)
'''
'''
#模拟鼠标的操作
a=dr.find_element_by_xpath('//*[@id="J_cate"]/ul')
for i in a:
    dd=dr.find_element_by_link_text(f'{i}')
    ActionChains(dr).move_to_element(dd).perform()
    sleep(1)
'''

#智能等待

# unt=ui.webDriverWait(dr,10)#创建一个智能等待
# unt.until(lambda dr:dr.find_element_by_xpath('//*[@id="lay"]/div[3]/div[1]/div[1]/ul').is_displayes())


#拖动
dr.switch_to.frame('login_frame')
sleep(2)
dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
sleep(2)
dr.find_element_by_xpath('//*[@id="u"]').send_keys('253456891')
sleep(2)
dr.find_element_by_xpath('//*[@id="p"]').send_keys('u658njiahfF')
sleep(2)
dr.find_element_by_xpath('//*[@id="login_button"]').click()
sleep(5)
dr.switch_to.frame('tcaptcha_iframe')
'''
drag_and_drop(起始位置,目的位置)可以定位到目的位置
drag_and_drop_by_offset(起始位置,x轴,y轴)不能定位到目的位置，用x和y定一个点
'''
ww = dr.find_element_by_xpath('//*[@id="tcaptcha_drag_button"]')
ActionChains(dr).drag_and_drop_by_offset(ww,170,0).perform()




sleep(5)
dr.quit()