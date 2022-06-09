import time
from appium import webdriver
from appium.webdriver.common.appiumby import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui as py
import pyperclip


desired_caps = dict(
    deviceName='Android',
    platformName='Android',
    dontStopAppOnReset=True,
    noReset=True,
    automationName='UiAutomator2',
    appPackage='com.android.chrome',
    appActivity='com.google.android.apps.chrome.Main',

)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
mb=['917010722560','918459214380']
for x in mb:
	driver.get("https://wa.me/"+x)
	driver.implicitly_wait(10)

	time.sleep(5)
	py.click(968,633)
	time.sleep(2)
	py.typewrite(x)
	time.sleep(2)
	py.doubleClick(969,420)
	time.sleep(2)
	py.click(1077,390)
	k = pyperclip.paste()
	time.sleep(2)

	if k==x:
	   print("valid")	
	   time.sleep(5)
	else:
	   print("not valid")   




