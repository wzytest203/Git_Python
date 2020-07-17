#!/usr/bin/python
# coding:utf-8      #添加中文注释，把编码统一成UTF-8,防止乱码
from selenium import webdriver  # 导入selenium的webdriver包；import所引入包，更专业的叫法为：模组（modules）
from time import sleep
from time import ctime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import autoit

driver = webdriver.Firefox()  # 将控制的webdriver的Firefox赋值给driver
# driver = webdriver.Chrome()
'''浏览器控制'''


def Browser_Control():
    driver.get("file:///C:/Users/Administrator/Desktop/web_test/index.html")  # get()方法，可以向浏览器发送网址
    # 出现urllib3.exceptions.MaxRetryError问题，执行pip install -U pyopenssl
    sleep(1)
    driver.minimize_window()  # 浏览器最小化
    sleep(1)
    driver.maximize_window()  # 浏览器最大化
    sleep(1)
    driver.set_window_size(800, 600)  # 设置浏览器大小
    sleep(1)
    driver.set_window_rect(x=600, y=500, width=600, height=400)  # 设置浏览器位置和大小
    # size_and_position = driver.get_window_rect()    #获取浏览器位置和大小
    # print('浏览器的大小和位置:', size_and_position)
    sleep(1)
    driver.maximize_window()  # 浏览器全屏化
    '''浏览器后退、前进'''
    first_url = 'https://www.baidu.com/'
    driver.get(first_url)
    sleep(3)
    second_url = 'http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html'
    driver.get(second_url)
    sleep(3)
    driver.back()  # 后退
    sleep(2)
    driver.forward()  # 前进
    sleep(1)
    driver.close()


'''webElement接口常用方法'''


def WebElement_Test():
    driver.get("https://www.baidu.com/")
    sleep(2)
    driver.find_element_by_xpath("//input[@id='kw']").send_keys("python")
    sleep(1)
    driver.find_element_by_xpath("//input[@id='kw']").clear()
    sleep(1)
    driver.find_element_by_xpath("//input[@id='kw']").send_keys("selenium")
    sleep(1)
    driver.find_element_by_xpath("//input[@id='kw']").submit()
    sleep(1)
    driver.find_element_by_link_text("百度首页").click()
    sleep(1)
    driver.quit()


'''打印信息'''


def Print_Message():
    driver.get("https://www.baidu.com/")
    sleep(2)
    title = driver.title  # 获取当前页面标题
    print title
    now_url = driver.current_url  # 获取当前页面url
    print now_url
    text = driver.find_element_by_xpath("//input[@id='su']").text  # 获取元素文本信息
    print text
    size = driver.find_element_by_xpath("//input[@id='su']").size  # 获取元素大小
    print size
    element = driver.find_element_by_xpath("//input[@id='su']").get_attribute("class")  # 获取元素class属性信息
    print element
    print(ctime())  # 获取当前时间
    driver.quit()


'''截图'''


def Screenshot():
    driver.get("https://www.baidu.com/")
    sleep(2)
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\upload\\cs1.png")
    driver.get_screenshot_as_file("C:\\Users\\Administrator\\Desktop\\upload\cs2.png")
    driver.quit()


'''等待时间'''


def Sleep_Time():
    driver.get("https://www.baidu.com/")
    sleep(2)
    driver.find_element_by_xpath("//input[@id='kw']").send_keys("python")
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//input[@id='kw']").clear()
    sleep(3)
    # element = WebDriverWait(driver,1,0.5).until(driver.find_element_by_id("kw"))
    # element.send_keys("selenium")
    driver.quit()


'''定位一组元素'''


def Checkboxs_Choose():  # 定位一组元素用elements,勾选所有复选框
    driver.get("file:///C:/Users/Administrator/Desktop/web_test/index.html")
    driver.implicitly_wait(3)
    # inputs = driver.find_elements_by_tag_name("input")
    # for a in inputs:
    #     if a.get_attribute('tpye') =="checkbox":
    #        a.click()
    #     sleep(1)
    checkboxs = driver.find_elements_by_xpath("//input[@type='checkbox']")
    for s in checkboxs:
        s.click()
        sleep(1)
    print(len(checkboxs))  # 输入checkboxs总个数
    driver.find_elements_by_xpath("//input[@type='checkbox']").pop().click()  # 把页面上最后一个checkbox勾去掉，使用pop（）或pop（-1）
    sleep(1)
    driver.find_elements_by_xpath("//input[@type='checkbox']").pop(0).click()  # 把页面上第一个checkbox勾去掉
    sleep(1)
    driver.find_elements_by_xpath("//input[@type='checkbox']").pop(1).click()  # 把页面上第二个checkbox勾去掉
    sleep(1)
    driver.quit()


'''弹窗处理'''


def Alert_Test():
    driver.get("file:///C:/Users/Administrator/Desktop/web_test/index.html")
    driver.implicitly_wait(3)
    driver.find_element_by_id("paycon").click()  # 提示对话框
    sleep(1)
    alert1 = driver.switch_to.alert
    print(alert1.text)
    alert1.accept()

    driver.implicitly_wait(3)
    driver.find_element_by_id("pay").click()  # 确认对话框
    sleep(1)
    confirm = driver.switch_to.alert
    print(confirm.text)
    confirm.dismiss()

    driver.implicitly_wait(3)
    driver.find_element_by_id("payin").click()  # 输入对话框
    prompt = driver.switch_to.alert
    print(prompt.text)
    prompt.send_keys(u"测试对话框")
    sleep(2)
    prompt.accept()
    driver.implicitly_wait(3)
    # alerta = driver.switch_to_alert()  #Python此类型选择alert或windows会出现警告
    alerta = driver.switch_to.alert
    print(alerta.text)
    alerta.accept()
    sleep(1)
    driver.quit()


'''鼠标事件'''


def Mouse_Test():  # 部门没有找到实例
    driver.get("file:///C:/Users/Administrator/Desktop/web_test/index.html")
    driver.implicitly_wait(10)
    # move_to_element  移动点击
    new_element = driver.find_element_by_xpath("//input[@id='CheckAll3']")  # 定位元素位置,定位第三个复选框
    ActionChains(driver).move_to_element(new_element).perform()  # 鼠标移动到定位元素上方进行点击
    sleep(2)
    driver.refresh()
    # 按下鼠标左键在一个元素上 ,和移动点击作用一致
    new1_element = driver.find_element_by_xpath("//input[@id='CheckAll3']")  # 定位元素位置,定位第三个复选框
    ActionChains(driver).click_and_hold(new1_element).perform()
    driver.refresh()
    sleep(2)
    # 双击
    double = driver.find_element_by_xpath("//input[@id='CheckAll3']")  # 定位元素位置,定位第三个复选框
    ActionChains(driver).double_click(double).perform()
    sleep(2)
    # 右键点击
    right = driver.find_element_by_xpath("//input[@id='CheckAll3']")  # 定位元素位置,定位第三个复选框
    ActionChains(driver).context_click(right).perform()
    sleep(2)

    # 拖拽
    # element1 = driver.find_element_by_link_text("国内")  #元素原位置
    # element2 = driver.find_element_by_link_text("国内")  #元素移动目标位置
    # ActionChains(driver).drag_and_drop(element1,element2).perform()
    driver.quit()


'''键盘事件'''


def Key_Board():
    driver.get("https://www.baidu.com/")
    sleep(2)
    driver.find_element_by_xpath("//input[@id='kw']").send_keys(u"selenium测试")  # 输入搜索内容
    driver.find_element_by_xpath("//input[@id='kw']").send_keys(Keys.CONTROL, 'a')  # 全选“selenium测试”
    driver.find_element_by_xpath("//input[@id='kw']").send_keys(Keys.CONTROL, 'c')  # 复制“selenium测试”
    sleep(1)
    driver.find_element_by_xpath("//input[@id='kw']").send_keys(Keys.SPACE)  # 敲击空格键
    sleep(2)
    driver.find_element_by_xpath("//input[@id='kw']").send_keys(Keys.BACK_SPACE)  # 敲击删除键
    driver.find_element_by_xpath("//input[@id='kw']").clear()  # 清空输入内容
    sleep(1)
    driver.find_element_by_xpath("//input[@id='kw']").send_keys(u"教程")  # 添加文字
    sleep(1)
    driver.find_element_by_xpath("//input[@id='kw']").send_keys(Keys.CONTROL, 'v')  # 粘贴“selenium测试”
    sleep(1)
    driver.find_element_by_xpath("//input[@id='kw']").send_keys(Keys.ENTER)  # 敲击回车键
    sleep(1)
    driver.quit()


'''上传文件'''


def Upload_Test():
    driver.get("file:///C:/Users/Administrator/Desktop/web_test/index.html")
    driver.implicitly_wait(3)
    driver.find_element_by_id("file").click()
    sleep(3)
    autoit.control_send(u"文件上传", "Edit1", "C:\\Users\\Administrator\\Desktop\\upload\\upload.png")
    sleep(1)
    autoit.control_click(u"文件上传", "Button1")  # 确定
    sleep(1)
    driver.find_element_by_xpath("//input[@id='file']").send_keys(
        "C:\\Users\\Administrator\\Desktop\\upload\\upload1.png")
    sleep(1)
    driver.quit()


# 调用模块执行
Browser_Control()
WebElement_Test()
Print_Message()
Screenshot()
Sleep_Time()
Checkboxs_Choose()
Alert_Test()
Mouse_Test()
Key_Board()
Upload_Test()
