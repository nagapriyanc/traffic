import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service(executable_path=r'C:\Users\LENOVO\Documents\traffic\chromedriver.exe')
driver = webdriver.Chrome()


for i in range(3):
	print(i)
	driver.get("http://google.com")
	time.sleep(5)

driver.quit()	