#!/usr/bin/python
# coding:utf-8
from selenium import webdriver
import time
from time import sleep


class Web_Search_Open(object):  # 创建类
    def Open_browser(self, driver):
        driver.get("https://www.baidu.com/")

    def Search_Selenium(self, driver):
        driver.implicitly_wait(5)
        driver.find_element_by_id("kw").send_keys("Selenium")
        driver.find_element_by_id("su").click()
        sleep(2)


class Web_Search_Close(object):  # 创建类
    def Search_Python(self, driver):
        driver.implicitly_wait(5)
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("Python")
        driver.find_element_by_id("su").click()
        sleep(2)

    def Close_browser(self, driver):
        driver.quit()
