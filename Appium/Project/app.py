import pytest
import capabilities
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

# desired_cap = {}
# desired_cap["platformName"] = "Android"
# desired_cap["platformVersion"] = "7"
# desired_cap["deviceName"] = "New Device g4"
# desired_cap["app"] = r"C:\Users\lendi\OneDrive\Desktop\Stack Overflow_1.0.0.1_Apkpure.apk"
# # desired_cap["appPackage"] = "com.code2lead.Stack Overflow_1.0.0.1_Apkpure"
# # desired_cap["appActivity"] = "com.code2lead.Stack Overflow_1.0.0.1_Apkpure.MainActivity"
#
# driver = webdriver.Remote(desired_cap)


desired_cap = {"platformName": "Android", "platformVersion": "7.0", "deviceName": "Test",
               "app": r"C:\APK files\Mahalaxmi Dindarshika 2023_41.0_Apkpure.apk",
               "appPackage": "com.mahalaxmi.marathi.pro", "appActivity": "com.mahalaxmi.marathi.pro.MainActivity"}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_capabilities=desired_cap)


# Converts capabilities to AppiumOptions instance
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)



