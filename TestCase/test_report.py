#!/usr/bin/python
#coding:utf-8
import unittest
from HTMLTestRunner import HTMLTestRunner  # py2适用


# import HTMLTestRunner
class Test_A(unittest.TestCase):

    def setUp(self):
        print ("test start")

    def test_selenium(self):
        print"hello selenium"

    def test_python(self):
        print"hello python"

    def tearDown(self):
        print ("test end")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test_A("test_selenium"))
    suite.addTest(Test_A("test_python"))
    fp = open("C:\\Users\\admin\Desktop\\HtmlTestRunner\\result1.html", 'wb')
    runner = HTMLTestRunner(stream=fp, title=u"测试报告", description=u"用例执行情况", verbosity=2)
    runner.run(suite)
    fp.close()