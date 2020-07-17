#!/usr/bin/python
# coding:utf-8
from selenium import webdriver
import time
from time import sleep

driver = webdriver.Chrome()


def Open_browser():
    driver.get("https://www.baidu.com/")


def Search_Selenium():
    driver.implicitly_wait(5)
    driver.find_element_by_id("kw").send_keys("Selenium")
    driver.find_element_by_id("su").click()
    sleep(2)


def Search_Python():
    driver.implicitly_wait(5)
    driver.find_element_by_id("kw").clear()
    driver.find_element_by_id("kw").send_keys("Python")
    driver.find_element_by_id("su").click()
    sleep(2)


def Close_browser():
    driver.quit()


'''调用模块'''
Open_browser()
Search_Selenium()
Search_Python()
Close_browser()
