#!/usr/bin/python
#coding:utf-8
from selenium import webdriver
import time
from time import sleep
from public.web_public import Web_Search_Open,Web_Search_Close
#引入public目录下web_public.py文件中的方法
driver = webdriver.Firefox()
Web_Search_Open().Open_browser(driver)
Web_Search_Open().Search_Selenium(driver)
Web_Search_Close().Search_Python(driver)
Web_Search_Close().Close_browser(driver)

