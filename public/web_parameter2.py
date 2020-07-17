#!/usr/bin/python
#coding:utf-8
from selenium import webdriver
from time import sleep
import time
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
'''读取txt文件进行参数化'''
test_txt = open("C:\\Users\\admin\\Desktop\\test.txt", "r")
lines = test_txt.readlines()
test_txt.close()
for line in lines:
    search_test1 = line.split(",")[0]
    search_test2 = line.split(",")[1]
    print(search_test1,search_test2)
    '''搜索search1'''
    driver.implicitly_wait(5)
    driver.find_element_by_id("kw").send_keys(search_test1)
    driver.find_element_by_id("su").click()
    driver.implicitly_wait(3)
    driver.find_element_by_id("kw").clear()
    sleep(2)
driver.quit()

