import time
from selenium import webdriver


driver = webdriver.Chrome(executable_path='')

#num of execution
count = 5

for i in range(count):
	print(i)
	driver.get("url of your site")
	#take some break
	time.sleep(10)
	print('opening site in Chrome')


driver.quit()	