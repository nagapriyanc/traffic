import time
from selenium import webdriver


driver = webdriver.Chrome(executable_path='')


for i in range(3):
	print(i)
	driver.get("url of your site")
	time.sleep(5)

driver.quit()	