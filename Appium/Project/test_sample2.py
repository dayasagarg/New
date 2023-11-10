import pytest
# import capabilities
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time
from appium.webdriver.common.touch_action import TouchAction
from appium_flutter_finder import FlutterElement, FlutterFinder


class TestApp:
    @pytest.fixture
    def setup_teardown(self):
        global driver
        desired_caps = {
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "platformVersion": "12",
            "deviceName": "Pixel_2",
            "app": r"C:\Users\lendi\OneDrive\Desktop\APK files\mitten\app-release.apk",
            "appPackage": "com.fintech.lenditt",
            "appActivity": "com.fintech.lenditt.MainActivity",

        }
        # "udid": "ZY2239JLP2"

        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        yield
        time.sleep(7)
        driver.quit()

    def test_prod_APK(self, setup_teardown):
        time.sleep(7)
        # login = FlutterElement(driver, FlutterFinder().by_semantics_label("Login"))

        # login = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(4)")

        # driver.find_element(AppiumBy.ID,"com.android.permissioncontroller:id/permission_allow_button").click()
        # time.sleep(2)
        login = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Login")
        # login = driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='login appbar Login']")
        login.click()
        #
        time.sleep(7)
        #
        windSize = driver.get_window_size()

        print("windSize::", windSize)
        print("context:", driver.context)
        deviceSize = driver.get_window_size()
        screenWidth = deviceSize['width']
        screenHeight = deviceSize['height']
        time.sleep(3)

        startx = screenWidth / 2
        endx = screenWidth / 2
        starty = screenHeight * 84 / 85
        endy = screenHeight / 85
        #
        # time.sleep(1)

        actions = TouchAction(driver)
        actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()
        time.sleep(5)
        actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()
        time.sleep(3)
        # driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector()).scrollIntoView(text("BUTTON15"))')
        # time.sleep(5)
        # #

        # scroll = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
        #                              'new UiScrollable(new UiSelector()).scrollIntoView(text("CIBIL"))')
        time.sleep(4)
        cibil = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "CIBIL")
        cibil.click()
        time.sleep(2)
        terms = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "T&C ")
        terms.click()
        time.sleep(2)
        terms_cls = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.ImageView")
        terms_cls.click()
        time.sleep(2)
        actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()
        actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()
        time.sleep(2)
        privacy = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "privacy policy.")
        privacy.click()
        time.sleep(2)
        priv_cls = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.ImageView")
        priv_cls.click()
        time.sleep(2)
        actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()
        actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()

        allow_access = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "permission-checkbox")
        allow_access.click()
        time.sleep(2)
        continueButton = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Continue")
        continueButton.click()
        time.sleep(2)

        MobileTextB = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
        MobileTextB.send_keys("1234567890")
        time.sleep(2)
        logContinueB = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(2)")
        # logContinueB = driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Continue']")
        logContinueB.click()
        time.sleep(2)
        otp = driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='pin-code-field']/android.view.View")
        otp.send_keys("1111")
        time.sleep(2)