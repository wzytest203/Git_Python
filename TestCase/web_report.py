#!/usr/bin/python
#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
from time import ctime
import autoit, os
# from unittest import TestCase
# # from unittest import TextTestRunner
# # from unittest import TestSuite
import unittest
# import HTMLTestRunner
from HTMLTestRunner import HTMLTestRunner  # py2适用


class Test_A(unittest.TestCase):

    def setUp(self):
        print"test start"

    def test_a(self):
        print"hello word"

    def test_b(self):
        print"welcome to china"

    def tearDown(self):
        print"test end"


class Test_B(unittest.TestCase):

    def setUp(self):
        print ("test start")
        self.driver = webdriver.Firefox()
        self.base_url = "file:///C:/Users/admin/Desktop/web_demo/index.html"

    def test_message(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.implicitly_wait(3)
        text = driver.find_element_by_id("payin").text  # 获取按钮文本信息
        print(text)
        element = driver.find_element_by_id("payin").get_attribute("onclick")  # 获取按钮onckick属性信息
        print(element)
        size = driver.find_element_by_id("ProductName").size
        print(size)

    def test_checkbox(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.implicitly_wait(3)
        driver.implicitly_wait(3)
        driver.find_element_by_xpath("//input[@id='CheckAll1']").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='CheckAll2']").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='CheckAll3']").click()
        sleep(1)
        driver.find_elements_by_xpath("//input[@type='checkbox']").pop().click()  # 操作最后的复选框
        sleep(1)
        driver.find_elements_by_xpath("//input[@type='checkbox']").pop(-1).click()  # 操作最后的复选框
        sleep(1)
        driver.find_elements_by_xpath("//input[@type='checkbox']").pop(0).click()  # 操作第一个复选框
        sleep(1)

    def test_checkboxs(self):  # 定位
        # 一组元素用elements
        driver = self.driver
        driver.get(self.base_url)
        driver.implicitly_wait(3)
        driver.implicitly_wait(3)
        inputs = driver.find_elements_by_tag_name("input")
        for a in inputs:
            if a.get_attribute('tpye') == "checkbox":
                a.click()
            sleep(1)
        checkboxs = driver.find_elements_by_xpath("//input[@type='checkbox']")
        for s in checkboxs:
            s.click()
            sleep(1)
            print(len(checkboxs))

    def test_ProductName(self):
        driver = self.driver
        driver.get(self.base_url)
        test_txt = open("C:\\Users\\admin\\Desktop\\test.txt", "r")
        lines = test_txt.readlines()
        test_txt.close()
        for line in lines:
            name = line.split(",")[0]
            tity = line.split(",")[1]
            print(name, tity)
            driver.implicitly_wait(3)
            driver.find_element_by_id("ProductName").clear()
            driver.find_element_by_id("ProductName").send_keys(name)
            sleep(1)
            driver.find_element_by_id("Quantity").clear()
            driver.find_element_by_id("Quantity").send_keys(tity)
            sleep(1)

    def tearDown(self):
        self.driver.quit()
        print ("test end")


class Test_C(unittest.TestCase):

    def setUp(self):
        print ("test start")
        self.driver = webdriver.Firefox()
        self.base_url = "https://www.baidu.com/"

    def test_selenium_search(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.implicitly_wait(3)
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
        sleep(2)

    def test_python_search(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.implicitly_wait(3)
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("python")
        driver.find_element_by_id("su").click()
        sleep(2)

    def tearDown(self):
        self.driver.quit()
        print ("test end")


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(Test_A("test_a"))
    suite.addTest(Test_A("test_b"))
    suite.addTest(Test_B("test_message"))
    suite.addTest(Test_B("test_checkbox"))
    suite.addTest(Test_B("test_checkboxs"))
    suite.addTest(Test_B("test_ProductName"))
    suite.addTest(Test_C("test_selenium_search"))
    suite.addTest(Test_C("test_python_search"))
    # runner = unittest.TextTestRunner()  #执行单个测试，即单元测试使用
    # runner.run(suite)
    fp = open("C:\\Users\\admin\Desktop\\HtmlTestRunner\\result3.html", 'wb')
    runner = HTMLTestRunner(stream=fp, title=u"测试页面测试报告", description=u"用例执行情况", verbosity=2)
    runner.run(suite)
    fp.close()

