import pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

# 所要爬取的页面地址
uri = ''
browser = webdriver.Chrome()
browser.get('http://www.chineseall.cn/org/index.action')
# 登入书香中国的账号！这一点很重要！！
time.sleep(30)
# 这里将272改变成你需要的pdf的页数
for i in range(272):
    browser.get(uri + str(i+1))
    pic = browser.find_element_by_id('bookContent')
    time.sleep(5)
    action = ActionChains(browser).move_to_element(pic)
    action.context_click(pic).perform()
    time.sleep(1)
    pyautogui.press('f12')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
browser.close()

