#1
from selenium import webdriver
import time

driver = webdriver.Chrome

driver.get("http://www.baidu.com")

driver.maximize_window()

driver.find_elements_by_id("kw").send_keys("我为什么这么帅？")

driver.find_element_by_id("su").click()

time.sleep(7)
driver.quit()

#2
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get(r"E:\python1\autom\day01\day01\资料\练习的html\练习的html\main.html")

driver.switch_to.frame("frame")

driver.find_element_by_id("input1").send_keys("123")
time.sleep(2)

driver.find_element_by_id("input1").clear()

time.sleep(3)
driver.quit()

#3
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get(r"E:\python1\autom\day01\day01\资料\练习的html\练习的html\弹框的验证/dialogs.html")
driver.find_element_by_id("alert").click()
time.sleep(3)
# 点击弹框的确定取消按钮     dismiss 取消
driver.switch_to.alert.accept()
time.sleep(3)
driver.quit()

#4
from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get(r"E:/python1/autom/day01/day01/资料/练习的html/练习的html/上传文件和下拉列表/autotest.html")
# 输入用户名
driver.find_element_by_xpath("//*[@id='accountID']").send_keys("zybr")
# 输入密码
driver.find_element_by_xpath("//*[@id='passwordID']").send_keys("123456")
# 地区
driver.find_element_by_xpath("//*[@id='areaID']").send_keys("北京市")
# 性别
driver.find_element_by_xpath("//*[@id='sexID2']").click()
# 季节
driver.find_element_by_xpath("//*[@value='spring']").click()
driver.find_element_by_xpath("//*[@value='winter']").click()

# 上传文件
driver.find_element_by_xpath("//*[@name='file' and @type='file']").send_keys(r"C:\Users\gsj\Pictures\Saved Pictures\嘿嘿.jpg")

time.sleep(3)
driver.quit()

