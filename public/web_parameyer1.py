#!/usr/bin/python
#coding:utf-8
from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
'''读取数组进行参数化'''
test_txt = ['test1','test2','test3','test4','test5']
for txt in test_txt:
    print(txt)
    '''搜索search'''
    driver.implicitly_wait(5)
    driver.find_element_by_id("kw").send_keys(txt)
    driver.find_element_by_id("su").click()
    sleep(1)
    driver.find_element_by_id("kw").clear()
    sleep(2)
driver.quit()
