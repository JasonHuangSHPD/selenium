# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
import pytest
from appium.webdriver.common.touch_action import TouchAction
import time

from appium.webdriver.extensions.android.gsm import GsmCallActions
from hamcrest import *



class TestDw():

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
        caps["avd"] = "Pixel_3_API_28"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(6)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
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
        current_price = float(self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/stockName' and @text='阿里巴巴']/../..//*[@resource-id='com.xueqiu.android:id/current_price']").text)
        expect_price = 220
        assert_that(current_price, close_to(expect_price, expect_price*0.2))
        assert current_price > 200

    def test_attr(self):
        """
        1. 打开雪球
        2.定位首页搜索框
        3.判断搜索框是否可用，并查看搜索框name的属性值
        4.打印搜索框这个元素的左上角坐标和它的高度
        5.向搜索框输入alibaba
        6.如果可见，打印搜索成功，如果不可见，打印搜索失败
        :return:
        """
        element = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        search_enabled =element.is_enabled()
        print(element.text)
        print(element.location)
        print(element.size)

        if search_enabled == True:
            element.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
            alibaba_element = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            print(alibaba_element.is_displayed())
            if alibaba_element.get_attribute("displayed") == "true":
                print("搜索成功")
            else:
                print("搜索失败")

    def test_touchaction(self):
        """
        触摸屏滑动
        :return:
        """
        action = TouchAction(self.driver)
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width * 1/2)
        y_start = int(height * 4/5)
        y_end = int(height * 1/5)
        action.press(x=x1, y=y_start).wait(500).move_to(x=x1, y=y_end).release().perform()

    def test_myinfo(self):
        """
        1. 点击我的，进入到个人信息页面
        2. 点击登录，进入到登录页面
        3. 输入用户名，输入密码
        4. 点击登录
        :return:
        """
        # self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("我的")').click()
        # time.sleep(3)
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("帐号密码登录")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("123456")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("123456")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()


    def test_scroll_find_element(self):
        """
        滚动查找
        :return:
        """
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector().text("热门帖子").instance(0));')

    def test_mobile(self):
        """
        1.程序运行中发送短信
        2.打电话
        3.切换网络
        4.截图
        :return:
        """
        # self.driver.make_gsm_call('13800001111', GsmCallActions.CALL)
        # self.driver.send_sms("13899998888", "hello appium api")
        self.driver.set_network_connection(1)
        time.sleep(3)
        self.driver.set_network_connection(4)
        self.driver.get_screenshot_as_file('./photos/img.png')
        time.sleep(3)

if __name__ == '__main__':
    pytest.main()
