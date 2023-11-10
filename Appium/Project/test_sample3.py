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
            "platformVersion": "14",
            "deviceName": "Redmi 10 Prime 2020",
            "app": r"C:\Users\lendi\OneDrive\Desktop\APK files\mitten\app-release_2.apk",
            "appPackage": "com.fintech.lenditt",
            "appActivity": "com.fintech.lenditt.MainActivity",
            "udid": "7aa117d30603"


        }

        # "udid": "ZY2239JLP2"

        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        yield
        time.sleep(7)
        driver.quit()

    def test_prod_APK(self, setup_teardown):
        time.sleep(3)
        # login = FlutterElement(driver, FlutterFinder().by_semantics_label("Login"))

        # login = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(4)")

        driver.find_element(AppiumBy.ID,"com.android.permissioncontroller:id/permission_allow_button").click()
        time.sleep(2)
        login = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Login")
        # login = driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='login appbar Login']")
        login.click()
        #
        time.sleep(5)
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
        starty = screenHeight * 9 / 9
        endy = screenHeight / 9
        #
        # time.sleep(11)

        actions = TouchAction(driver)
        actions.long_press(None,startx,starty).move_to(None,endx,endy).release().perform()
        # time.sleep(5)
        actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()
        time.sleep(3)
        # driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector()).scrollIntoView(text("BUTTON15"))')
        # time.sleep(5)
        # #

        # scroll = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
        #                              'new UiScrollable(new UiSelector()).scrollIntoView(text("CIBIL"))')
        time.sleep(4)
        cibil = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"CIBIL")
        cibil.click()
        time.sleep(2)
        terms = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"T&C ")
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
        time.sleep(2)

        allow_access = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "permissioncheckbox")
        allow_access.click()
        time.sleep(2)
        continueButton = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Continue")
        continueButton.click()
        time.sleep(2)

        MobileTextB = driver.find_element(AppiumBy.CLASS_NAME,"android.widget.EditText")
        MobileTextB.send_keys("1234567890")
        time.sleep(2)
        logContinueB = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"UiSelector().index(2)")
        # logContinueB = driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Continue']")
        logContinueB.click()

        time.sleep(2)
        # edit = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"edit_number_mail Edit")
        edit = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"UiSelector().index(2)")
        edit.click()
        time.sleep(3)
        edit_continue = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"UiSelector().index(2)")
        edit_continue.click()
        # time.sleep(67)
        # resend_otp = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"UiSelector().index(4)")
        # resend_otp.click()
        time.sleep(5)


        driver.press_keycode(8)
        driver.press_keycode(8)
        driver.press_keycode(8)
        driver.press_keycode(8)

        time.sleep(5)
        #
        # referal_code = driver.find_element(AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]")
        # referal_code.send_keys("123456")
        # apply = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Apply")
        # apply.click()
        # time.sleep(2)
        # skip = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Skip")
        skip = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"UiSelector().index(9)")
        skip.click()
        time.sleep(2)
        whilUseApp = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
        whilUseApp.click()
        time.sleep(2)









