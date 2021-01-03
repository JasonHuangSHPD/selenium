from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *


class TestToast():
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "33"
        caps["appPackage"] = "io.appium.android.apis"
        caps["appActivity"] = "io.appium.android.apis.view.PopupMenu1"
        caps["automationName"] = "uiautomator2"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(6)

    def teardown(self):
        self.driver.quit()

    def test_toast(self):
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID,"Make a Popup!").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='Search']").click()
        # print(self.driver.page_source)
        print(self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text)
        print(self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, 'Clicked popup menu item Search')]").text)
