from selenium import webdriver
from time import sleep

'''
#QQ邮箱发邮件
dr=webdriver.Chrome()
dr.get('https://mail.qq.com/')#打开QQ邮箱网页
sleep(3)
dr.switch_to.frame('login_frame')#切换到内嵌框架
dr.find_element_by_id('img_out_1148389400').click()#点击头像登录邮箱
sleep(3)
dr.find_element_by_id('composebtn').click()#点击写信按钮
sleep(3)
dr.switch_to.frame('mainFrame')#切换到信纸框架
sleep(1)
dr.find_element_by_xpath('/html/body/form[2]/div[2]/div[3]/div[2]/table[2]/tbody/tr/td[2]/div[1]/div[2]/input').send_keys('13750712917@163.com')#填写收件人
sleep(1)
dr.find_element_by_xpath('//*[@id="subject"]').send_keys('这是用Python写的邮件')#填写邮件主题
sleep(1)
dr.switch_to.frame(dr.find_element_by_class_name("qmEditorIfrmEditArea"))#dr.find_element_by_class_name("qmEditorIfrmEditArea")
dr.find_element_by_xpath('/html/body').send_keys('这是我使用Python写的邮件')#邮件正文
sleep(1)
dr.switch_to.parent_frame()#退回到上层框架
sleep(1)
dr.find_element_by_xpath('//*[@id="toolbar"]/div/a[1]').click()
sleep(5)
dr.switch_to.parent_frame()
dr.find_element_by_xpath('//*[@id="SetInfo"]/div[1]/a[3]').click()
sleep(5)
dr.quit()
'''

#网易云音乐
dr=webdriver.Chrome()
dr.get('https://music.163.com/')
sleep(5)
dr.find_element_by_xpath('//*[@id="g-topbar"]/div[1]/div/ul/li[2]/span/a/em').click()
sleep(3)
dr.switch_to.frame('contentFrame')
sleep(3)
dr.find_element_by_xpath('/html/body/div[3]/div/div/a').click()
sleep(3)
dr.switch_to.default_content()#退回到最底层框架
sleep(3)
dr.switch_to.frame(dr.find_element_by_class_name("auto-1566704079882 m-layer z-show"))
dr.find_element_by_xpath('//*[@id="auto-id-xGE2VIDAkan1TIwa"]/div/div[2]/ul/li[2]/a').click()
