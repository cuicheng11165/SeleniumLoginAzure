# -*- coding: utf-8 -*-  

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pickle
import time
from sys import stdin
from DataDriver import DataDriver
import datetime

class LoginBase(object):
    def __init__(self):
        self.data_driver = DataDriver()
        self.driver = webdriver.Chrome(self.data_driver.driver_location) # 指定ChromeDriver，用Chrome来测试当前网址


class AzureLogin(LoginBase):
    def __init__(self):
        LoginBase.__init__(self)

    def login(self):
        target_url= self.data_driver.gao_portal_url
                
        self.driver.get(target_url) # 打开一个新的浏览器窗口，并跳到相应的URL
        logininput = self.driver.find_element_by_name("loginfmt")#找到Login的InputText        
        logininput.send_keys(self.data_driver.login_user_name)#模拟输入用户名行为
 

        time.sleep(2)

        next_input = self.driver.find_element_by_id("idSIButton9")#找到Login的InputText
        next_input.click()#模拟点击Next

        time.sleep(2)

        passwordinput = self.driver.find_element_by_name("passwd")#模拟输入密码行为
        passwordinput.send_keys(self.data_driver.login_user_password)#模拟输入密码

        time.sleep(2)

        signin_input = self.driver.find_element_by_id("idSIButton9")
        signin_input.click()#模拟点击Next

        time.sleep(1)

        staysignin_input = self.driver.find_element_by_id("idSIButton9")
        staysignin_input.click()#模拟点击Yes

        time.sleep(1)

        self.save_cookie()
        
        # self.driver.close()#把Cookie信息持久化之后关闭浏览器

    def save_cookie(self):        
        cookies=self.driver.get_cookies()
        cookie_entity = {}
        cookie_entity['login_time']=datetime.datetime.now()
        cookie_entity['entry']=cookies

        with open('Cookies\\sso\\{0}.txt'.format(self.data_driver.login_user_name), 'wb') as cookie_file:
            pickle.dump(cookie_entity,cookie_file)

        cookie_file.close()

    
    def read_cookie(self):
        cookie_file = open("Cookies\\sso\\{0}.txt".format(self.data_driver.login_user_name),'rb')
        cookies_instance=pickle.load(cookie_file,fix_imports=True)      

        login_time=cookies_instance['login_time']
        
        time_diff = datetime.datetime.now()-login_time

        cookies_entry=cookies_instance['entry']

        if time_diff.seconds > 3600 or cookies_entry is None:         
            self.login()
        else:            
            self.driver.get(self.data_driver.gao_portal_url)

            for cookie in cookies_entry:
                self.driver.add_cookie(cookie)

            self.driver.get(self.data_driver.gao_portal_url)  
         

class AosLogin(LoginBase):
    def __init__(self):
       LoginBase.__init__(self)

    def login(self):
        target_url=self.data_driver.aos_portal_url

            
        self.driver.get(target_url) # 打开一个新的浏览器窗口，并跳到相应的URL

        logininput = self.driver.find_element_by_class_name("O365-button-container")
        logininput.click()

        logininput = self.driver.find_element_by_name("loginfmt")#找到Login的InputText        
        logininput.send_keys(self.data_driver.login_user_name)#模拟输入用户名行为
 
        time.sleep(2)

        next_input = self.driver.find_element_by_id("idSIButton9")#找到Login的InputText
        next_input.click()#模拟点击Next

        time.sleep(2)

        passwordinput = self.driver.find_element_by_name("passwd")#模拟输入密码行为
        passwordinput.send_keys(self.data_driver.login_user_password)#模拟输入密码

        time.sleep(2)

        signin_input = self.driver.find_element_by_id("idSIButton9")
        signin_input.click()#模拟点击Next

        time.sleep(1)

        staysignin_input = self.driver.find_element_by_id("idSIButton9")
        staysignin_input.click()#模拟点击Yes

        time.sleep(1)

        staysignin_input = self.driver.find_element_by_class_name("GovernanceAutomation")
        staysignin_input.click()#模拟点击Yes
        
        gao_window=self.driver.window_handles[1]

        self.driver.switch_to_window(gao_window)

        self.save_cookie()
        
        # self.driver.close()#把Cookie信息持久化之后关闭浏览器

    def save_cookie(self):        
        cookies=self.driver.get_cookies()
        cookie_entity = {}
        cookie_entity['login_time']=datetime.datetime.now()
        cookie_entity['entry']=cookies

        with open('Cookies\\aos\\{0}.txt'.format(self.data_driver.login_user_name), 'wb') as cookie_file:
            pickle.dump(cookie_entity,cookie_file)
        cookie_file.close()


    def read_cookie(self):
        cookie_file = open("Cookies\\aos\\{0}.txt".format(self.data_driver.login_user_name),'rb')
        cookies_instance=pickle.load(cookie_file,fix_imports=True)      

        login_time=cookies_instance['login_time']
        
        time_diff = datetime.datetime.now()-login_time

        cookies_entry=cookies_instance['entry']

        if time_diff.seconds > 3600 or cookies_entry is None:         
            self.login()
        else:            
            self.driver.get(self.data_driver.gao_portal_url)

            for cookie in cookies_entry:
                self.driver.add_cookie(cookie)

            self.driver.get(self.data_driver.gao_portal_url)  
         


                