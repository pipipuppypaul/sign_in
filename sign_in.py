#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

myusername = "account"#帐号
mypassword = "password"#密码

driver = webdriver.Chrome('./chromedriver')#chromedriver.exe放在当前文件夹
driver.get("http://gre.kmf.com/")#输入你自己要访问的网站，这里以GRE考满分为例
content = driver.find_element_by_css_selector("a[popup='login']").click()

time.sleep(3)
try:
    #driver.switch_to.frame(0)
    acount = driver.find_element_by_css_selector("input[id='LoginPopupName']")
    acount.clear()
    acount.send_keys(myusername)
    time.sleep(1)

    password = driver.find_element_by_css_selector("input[id='LoginPopupPassword']")
    password.clear()
    password.send_keys(mypassword)
    time.sleep(1)
    
    driver.find_element_by_css_selector("a[id='LoginSubmit']").click()
except:
    print('login fail')
    
    
try:
    time.sleep(3)
    sign = driver.find_element_by_css_selector("a[class='punch-btn front  punch-btn-bg']")
    sign.click()
except:
    print('signing fail')

