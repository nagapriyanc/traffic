from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def go():
    global driver,e
    opts = Options()
    s = Service(r'C:\Users\LENOVO\PycharmProjects\traffic\chromedriver.exe')
    opts.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
    driver = webdriver.Chrome(options=opts, service=s)
    driver.get('https://autobacklinkbuilder.com/freebacklinks/links.php')
    time.sleep(3)
    driver.find_element(By.ID, 'url').send_keys('www.oxnrich.com')
    driver.find_element(By.ID, 'keyword').send_keys('oxnrich')
    driver.find_element(By.ID, 'limit').send_keys('2,500 Backlinks')
    driver.find_element(By.ID, 'button').click()
    time.sleep(5)
    driver.switch_to.new_window('tab')
    driver.get('https://autobacklinkbuilder.com/freebacklinks/links.php')
    time.sleep(3)
    driver.find_element(By.ID, 'url').send_keys('www.oxnrich.com')
    driver.find_element(By.ID, 'keyword').send_keys('oxnrich')
    driver.find_element(By.ID, 'limit').send_keys('2,500 Backlinks')
    driver.find_element(By.ID, 'button').click()
    time.sleep(5)
    driver.switch_to.new_window('tab')
    driver.get('https://autobacklinkbuilder.com/freebacklinks/links.php')
    time.sleep(3)
    driver.find_element(By.ID, 'url').send_keys('www.oxnrich.com')
    driver.find_element(By.ID, 'keyword').send_keys('oxnrich')
    driver.find_element(By.ID, 'limit').send_keys('2,500 Backlinks')
    driver.find_element(By.ID, 'button').click()
    time.sleep(5)
    global i,tabs
    tabs = driver.window_handles
    i = 1
    print(i)
    reset(i)

def reset(i):
    for tab in tabs:
        driver.switch_to.window(tab)
        time.sleep(5)
        driver.find_element(By.ID, 'button').click()
    i+= 1
    loop(i)

def loop(i):

    for tab in tabs:
        driver.switch_to.window(tab)
        time.sleep(2)
        driver.find_element(By.ID, 'url').send_keys('www.oxnrich.com')
        driver.find_element(By.ID, 'keyword').send_keys('oxnrich')
        driver.find_element(By.ID, 'limit').send_keys('2,500 Backlinks')
        driver.find_element(By.ID, 'button').click()
        time.sleep(5)
    time.sleep(5)

    print(i)
    if i == 2:
        close()
    else:
        reset(i)


def close():
    print("execution done")
    driver.quit()

if __name__ == "__main__":
   print("call go function")
   go()