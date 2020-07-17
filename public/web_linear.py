#!/usr/bin/python
#coding:utf-8
from selenium import webdriver
import time
from time import sleep
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
'''搜索selenium'''
driver.implicitly_wait(5)
driver.find_element_by_id("kw").send_keys("Selenium")
driver.find_element_by_id("su").click()
sleep(2)
'''搜索python'''
driver.implicitly_wait(5)
driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("Python")
driver.find_element_by_id("su").click()
sleep(2)
driver.quit()
