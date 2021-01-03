from appium import webdriver


class TestTouchAction():
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "33"
        caps["appPackage"] = "cn.kmob.screenfingermovelock"
        caps["appActivity"] = "com.samsung.ui.MainActivity"
        caps["noReset"] = "true"
        # caps["dontStopAppOnReset"] = "true"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(6)

    def teardown(self):
        self.driver.quit()

    def test_touchaction_unlock(self):
        pass
