# -*- coding:utf-8 -*-
from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument('headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(chrome_options=option)
# driver = webdriver.Chrome()
# driver = webdriver.PhantomJS()
driver.get('https://shop.bidcms.com/')
print(u'打开浏览器')
print(driver.title)
driver.find_element_by_id('ipt_account').send_keys(u'13800000000')
driver.find_element_by_id('ipt_pwd').send_keys(u'limengqi')
driver.find_element_by_id('ipt_code').send_keys(u'1234')
login = driver.find_element_by_xpath('//button[contains(@class, "ng-isolate-scope")]');
print(login.text)
login.click()
print(u'关闭')
driver.quit()
print(u'测试完成')