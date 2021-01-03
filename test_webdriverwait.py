from appium import webdriver
import pytest
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait():

    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "33"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".common.splash.SplashActivity"
        caps["noReset"] = "true"
        # caps["dontStopAppOnReset"] = "true"
        caps["skipDeviceInitialization"] = "true"
        caps["unicldeKeyBoard"] = "true"
        caps["resetKeyBoard"] = "true"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(6)

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        """
        1. 打开雪球
        2. 点击搜索输入框
        3. 向搜索输入框内输入“阿里巴巴”
        4. 在搜索结果里面选择“阿里巴巴”，然后进行点击
        5. 获取这只阿里巴巴的股份，并判断这只股份的价格〈〉200
        :return:
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        locator = (MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/stockName' and @text='阿里巴巴']/../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        ele = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*locator))
        # ele = self.driver.find_element(*locator)
        print(ele.text)
        current_price = float(ele.text)
        expect_price = 170
        assert current_price > expect_price
