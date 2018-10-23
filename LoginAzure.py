# -*- coding: utf-8 -*-  

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pickle
import time
from sys import stdin

class AzureLogin(object):
    def __init__(self,driver_location):
        self.driver = webdriver.Chrome('D:\\tool\\webtest\\chromedriver_win32\\chromedriver.exe') # 指定ChromeDriver，用Chrome来测试当前网址

    def login(self,target_url,user_name,password):
        self.user_name=user_name                        
        self.driver.get(target_url) # 打开一个新的浏览器窗口，并跳到相应的URL
        logininput = self.driver.find_element_by_name("loginfmt")#找到Login的InputText        
        logininput.send_keys(user_name)#模拟输入用户名行为
 

        time.sleep(2)

        next_input = self.driver.find_element_by_id("idSIButton9")#找到Login的InputText
        next_input.click()#模拟点击Next

        time.sleep(2)

        passwordinput = self.driver.find_element_by_name("passwd")#模拟输入密码行为
        passwordinput.send_keys(password)#模拟输入密码

        time.sleep(2)

        signin_input = self.driver.find_element_by_id("idSIButton9")
        signin_input.click()#模拟点击Next

        time.sleep(1)

        staysignin_input = self.driver.find_element_by_id("idSIButton9")
        staysignin_input.click()#模拟点击Yes

        time.sleep(1)

        self.save_cookie()
        
        self.driver.close()#把Cookie信息持久化之后关闭浏览器

    def save_cookie(self):        
        cookies=self.driver.get_cookies()
        with open('{0}.txt'.format(self.user_name), 'wb') as cookie_file:
            pickle.dump(cookies,cookie_file)
        cookie_file.close()

        