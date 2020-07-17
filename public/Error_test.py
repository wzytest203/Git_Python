#!/usr/bin/python
#coding:utf-8
#方法一：try.... except+异常类名
try:
    test_txt = open("C:\\Users\\admin\\Desktop\\test1.txt", "r")
except IOError:
    print ("这是一个文件打开异常")
#方法二：try.... except  Exception  万能异常
try:
    test_txt = open("C:\\Users\\admin\\Desktop\\test1.txt", "r")
except Exception as e:
    print(e)
#方法三：try.... except ....finally  不管是否异常执行finally下语句
try:
    test_txt = open("C:\\Users\\admin\\Desktop\\test1.txt", "r")
except Exception as e:
    print(e)
finally:
    test_txt = open("C:\\Users\\admin\\Desktop\\test.txt", "r")
    test_txt.close()
    print("不管是否异常，都执行")






