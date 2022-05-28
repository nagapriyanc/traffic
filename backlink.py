from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Backlink:
        
    def __init__(self):
        global driver,e,i,tabs

        self.url = str(input("Enter url : "))
        self.keyword = str(input("Enter keyword: "))
        self.k = int(input("Enter number of time execute: "))
        driver = webdriver.Chrome()
       
    def go(self,x):
        for t in range(x):
            driver.get('https://autobacklinkbuilder.com/freebacklinks/links.php')
            time.sleep(3)
            driver.find_element(By.ID, 'url').send_keys(self.url)
            driver.find_element(By.ID, 'keyword').send_keys(self.keyword)
            driver.find_element(By.ID, 'limit').send_keys('2,500 Backlinks')
            driver.find_element(By.ID, 'button').click()
            time.sleep(5)
            
            if t!=2:
                driver.switch_to.new_window('tab')
        

    def reset(self,i):
        tabs = driver.window_handles
        for tab in tabs:
            driver.switch_to.window(tab)
            time.sleep(5)
            driver.find_element(By.ID, 'button').click()
        i+= 1
        self.loop(i,tabs)

    def loop(self,i,tabs):
        b=self.k
        
        if i == b:
            self.close()
        else :
            for tab in tabs:
                driver.switch_to.window(tab)
                time.sleep(2)
                driver.find_element(By.ID, 'url').send_keys(self.url)
                driver.find_element(By.ID, 'keyword').send_keys(self.keyword)
                driver.find_element(By.ID, 'limit').send_keys('2,500 Backlinks')
                driver.find_element(By.ID, 'button').click()
                time.sleep(5)
            self.reset(i)


    def close(self):
        print("execution done")
        driver.quit()


if __name__ == "__main__":

   obj = Backlink()
   obj.go(3)
   obj.reset(0)
