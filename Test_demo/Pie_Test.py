#!/usr/bin/python
# coding:utf-8
from time import sleep
import autoit


def open_pie():  # 启动PIE
    autoit.run(u"D:\\PIE自动化\\PIE(教学版)_enu20160701\\Release\\PIE.exe")  # 启动PIE
    autoit.win_wait_active(u"PIE(教学版", 30)  # 等待title窗口活跃，20秒超时
    # autoit.win_activate(u"PIE(教学版)")                                      #等待Title窗口出现


def win_conrrol():  # windows窗口控制
    '''窗口操作使用autoit调用autoit.Properties下方法,如下'''
    autoit.win_set_state(u"PIE(教学版)", autoit.autoit.Properties.SW_HIDE)  # 窗口隐藏
    sleep(2)
    autoit.win_set_state(u"PIE(教学版)", autoit.autoit.Properties.SW_SHOW)  # 窗口显示
    sleep(2)
    autoit.win_set_state(u"PIE(教学版)", autoit.autoit.Properties.SW_MINIMIZE)  # 窗口最小化
    sleep(2)
    autoit.win_set_state(u"PIE(教学版)", autoit.autoit.Properties.SW_MAXIMIZE)  # 窗口最大化
    sleep(3)
    '''使用from...autoit import Properties后直接使用，如下'''
    # autoit.win_set_state(u"PIE(教学版)", Properties.SW_HIDE)


def add_data_jpg():  # 加载栅格数据jpg格式
    '''添加数据方法一：设置焦点进行传参，添加jpg数据'''
    autoit.mouse_click("left", 54, 92, 1)  # 点击加载栅格数据
    autoit.win_wait_active(u"打开栅格文件", 15)  # 等待窗口活跃，15秒超时
    autoit.control_focus(u"打开栅格文件", "[Class:Edit; instance:1]")  # 设置焦点
    autoit.control_set_text(u"打开栅格文件", "[Class:Edit; instance:1]", "C:\Users\Administrator\Desktop\GF1.jpg")
    # 输入文本
    autoit.control_click(u"打开栅格文件", "Button1")
    sleep(5)


def add_data_tif():  # 加载栅格数据Tif格式，此格式是否需要建立金字塔

    '''添加数据方法二：直接使用control_set_text传参，添加tif数据是否建立金字塔'''
    autoit.mouse_click("left", 50, 92, 1)  # 点击加载栅格数据
    autoit.win_wait_active(u"打开栅格文件", 15)
    autoit.control_set_text(u"打开栅格文件", "Edit1", r"C:\Users\admin\Desktop\PIEDATA\GF1.tiff")
    autoit.control_click(u"打开栅格文件", "Button1")  # 确定打开文件
    autoit.win_wait_active(u"建立金字塔", 5)  # 等待是否建立金字塔窗口
    autoit.control_click(u"建立金字塔", "Button3")  # 取消建立金字塔
    sleep(10)

    '''添加数据方法三：使用control_send传参，添加tif数据是否建立金字塔'''
    # autoit.control_send(u"打开栅格文件","Edit1","C:\\Users\\admin\\Desktop\\PIEDATA\\GF1.tiff",1)
    # #mode= 0 （默认），按键序列中含有的特殊字符比如 + 和 ! 将被视为 SHIFT 和 ALT 键。
    # #mode= 1，按键将按原样发送。


def add_data_shp():  # 加载矢量数据shp格式
    autoit.mouse_click("left", 120, 92, 1)  # 点击加载矢量数据
    autoit.win_wait_active(u"打开矢量文件", 15)
    autoit.control_set_text(u"打开矢量文件", "Edit1", r"C:\Users\admin\Desktop\PIEDATA\Lambert_SHP\beijing.shp")
    autoit.control_click(u"打开矢量文件", "Button1")  # 选择好文件，点击打开
    autoit.win_wait_active(u"提示", 5)  # 不同坐标系，提示是否新建图层
    autoit.control_click(u"提示", "Button2")  # 新建图层
    sleep(5)


def right_control():  # 图层右键功能
    autoit.mouse_click("Right", 93, 193, 1, 10)  # 右键点击图层，打开功能列表
    sleep(1)
    autoit.send("{down 10}")  # 选择第十行，选择属性
    sleep(1)
    autoit.send("{enter}")
    autoit.win_wait_active(u"图层属性", 5)  # 等待图层属性窗口，5秒超时
    sleep(1)
    autoit.control_click(u"图层属性", "Button2")  # 关闭图层属性
    sleep(1)


def view_management():  # 视图管理
    autoit.mouse_click("LEFT", 85, 40, 1, 10)  # 进入视图管理模块
    sleep(1)

    autoit.mouse_click("LEFT", 460, 92, 1, 10)  # 拉狂放大
    autoit.mouse_click_drag(650, 170, 850, 400, "LEFT", 20)
    sleep(1)

    autoit.mouse_click("LEFT", 520, 92, 1, 10)  # 拉狂缩小
    autoit.mouse_click_drag(650, 170, 850, 400, "LEFT", 20)
    sleep(1)

    autoit.mouse_click("LEFT", 570, 92, 1, 10)  # 点击中心放大，点击1次
    sleep(1)

    autoit.mouse_click("LEFT", 620, 92, 2, 10)  # 点击中心缩小，点击2次
    sleep(1)

    autoit.mouse_click("LEFT", 670, 92, 1, 10)  # 漫游
    autoit.mouse_click_drag(800, 350, 400, 350, "LEFT", 20)
    sleep(1)
    autoit.mouse_click_drag(400, 350, 800, 350, "LEFT", 20)
    sleep(1)

    autoit.mouse_click("LEFT", 750, 92, 1, 10)  # 1:1显示
    sleep(1)

    autoit.mouse_click("LEFT", 710, 92, 1, 10)  # 1:1全图
    sleep(1)

    autoit.mouse_click("LEFT", 800, 92, 1, 10)  # 卷帘
    autoit.mouse_click_drag(400, 350, 1000, 350, "LEFT", 20)
    sleep(1)
    autoit.mouse_click_drag(1000, 350, 400, 350, "LEFT", 20)
    sleep(1)

    autoit.mouse_click("LEFT", 850, 70, 1, 10)  # 图层管理打开关闭
    sleep(1)
    autoit.mouse_click("LEFT", 850, 70, 1, 10)
    sleep(1)

    autoit.mouse_click("LEFT", 850, 110, 1, 10)  # 鹰眼打开关闭
    sleep(1)
    autoit.mouse_click("LEFT", 850, 110, 1, 10)
    sleep(1)


def display_control():  # 显示控制模块
    autoit.mouse_click("LEFT", 160, 40, 1, 10)  # 进入显示控制模块
    sleep(1)

    '''亮度增强'''
    autoit.mouse_click_drag(119, 92, 150, 92, "LEFT", 1)  # 亮度增强，向右拖拽
    sleep(1)
    autoit.mouse_click_drag(150, 92, 80, 92, "LEFT", 1)  # 亮度增强，向左拖拽
    sleep(1)
    autoit.mouse_click("LEFT", 60, 92, 1, 10)  # 亮度增强，点击“-”1次
    sleep(1)
    autoit.mouse_click("LEFT", 175, 92, 2, 10)  # 亮度增强，点击“+”2次
    sleep(1)
    autoit.mouse_click("LEFT", 30, 92, 1, 10)  # 亮度增强，点击“亮度”恢复原状

    '''对比度增强'''
    autoit.mouse_click_drag(305, 92, 340, 92, "LEFT", 1)  # 对比度增强，向右拖拽
    sleep(1)
    autoit.mouse_click_drag(340, 92, 270, 92, "LEFT", 1)  # 对比度增强，向左拖拽
    sleep(1)
    autoit.mouse_click("LEFT", 245, 92, 1, 10)  # 对比度增强，点击“-”1次
    sleep(1)
    autoit.mouse_click("LEFT", 360, 92, 2, 10)  # 对比度增强，点击“+”2次
    sleep(1)
    autoit.mouse_click("LEFT", 220, 92, 1, 10)  # 对比度增强，点击“对比度”恢复原状

    '''透明度增强'''
    autoit.mouse_click_drag(450, 92, 510, 92, "LEFT", 1)  # 透明度增强，向右拖拽
    sleep(1)
    autoit.mouse_click_drag(510, 92, 480, 92, "LEFT", 1)  # 透明度增强，向左拖拽
    sleep(1)
    autoit.mouse_click("LEFT", 435, 92, 1, 10)  # 透明度增强，点击“-”1次
    sleep(1)
    autoit.mouse_click("LEFT", 555, 92, 2, 10)  # 透明度增强，点击“+”2次
    sleep(1)
    autoit.mouse_click("LEFT", 405, 92, 1, 10)  # 透明度增强，点击“透明度”恢复原状

    '''拉伸方式'''

    autoit.mouse_click("LEFT", 745, 92, 1, 10)  # 点击拉伸方式,展开下拉列表
    sleep(1)
    autoit.send("{up 5}")  # 切换到下拉列表第一位
    autoit.send("{enter}")  # 确定选择
    sleep(1)  # 1%线性拉伸

    autoit.mouse_click("LEFT", 745, 92, 1, 10)  # 点击拉伸方式,展开下拉列表
    sleep(1)
    autoit.send("{up 5}")  # 切换到下拉列表第一位
    sleep(1)
    autoit.send("{down 1}")  # 选择下拉列表第二位
    sleep(1)
    autoit.send("{enter}")  # 确定选择
    sleep(1)  # 2%线性拉伸

    '''视图联动与拉伸方式类似'''


def close_pie():  # 关闭pie窗口
    autoit.win_close(u"PIE(教学版)")
    sleep(2)
    autoit.control_click("[class:#32770]", "Button2")  # 不保存工程


def close_pie_process_close():  # 关闭pie进程
    sleep(2)
    autoit.process_close("PIE.exe")
    sleep(1)


open_pie()  # 打开PIE
win_conrrol()  # windows窗口控制
add_data_jpg()  # 加载栅格数据jpg
# add_data_tif()                 #加载栅格数据tif
# add_data_shp()                 #加载矢量数据
right_control()  # 图层右键功能
view_management()  # 视图管理
display_control()  # 显示控制
# close_pie()                    #关闭PIE窗口
close_pie_process_close()  # 关闭PIE进程
