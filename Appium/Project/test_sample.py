import pytest
# import capabilities
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time



class TestApp:
    @pytest.fixture
    def setup_teardown(self):
        global driver
        desired_caps = {
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "platformVersion": "12",
            "deviceName": "Pixel_2",
            "app": r"C:\Users\lendi\OneDrive\Desktop\APK files\sample apk\Mahalaxmi Dindarshika 2023_41.0_Apkpure.apk",
            "appPackage": "com.mahalaxmi.marathi.pro",
            "appActivity": "com.mahalaxmi.marathi.pro.MainActivity",

        }
        # "udid": "ZY2239JLP2"

        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        yield
        time.sleep(3)
        driver.quit()

    def test_prod_APK(self, setup_teardown):
        ele_id = driver.find_element(AppiumBy.ID, "com.mahalaxmi.marathi.pro:id/imageViewVarshikAlokan")
        ele_id.click()
        time.sleep(3)
