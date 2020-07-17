#!/usr/bin/python
#coding:utf-8
from selenium import webdriver
from time import sleep
import csv
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
'''读取csv文件进行参数化'''
test_txt = csv.reader(open("C:\\Users\\admin\\Desktop\\test.csv", "r"))
for txt in test_txt:
    search1 = txt[0]
    search2 = txt[1]
    print(search1,search2)
    '''搜索search1'''
    driver.implicitly_wait(5)
    driver.find_element_by_id("kw").send_keys(search1)
    driver.find_element_by_id("su").click()
    sleep(1)
    driver.find_element_by_id("kw").clear()
    sleep(2)
driver.quit()
