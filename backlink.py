from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


def go():
    global driver,e
    driver = webdriver.Chrome(executable_path='C:\\Users\\LENOVO\\PycharmProjects\\facebook\\chromedriver.exe')
    e1 = driver.current_window_handle
    e = [e1]
    driver.get('https://autobacklinkbuilder.com/freebacklinks/links.php')
    time.sleep(3)
    driver.find_element(By.ID, 'url').send_keys('www.oxnrich.com')
    driver.find_element(By.ID, 'keyword').send_keys('oxnrich')
    driver.find_element(By.ID, 'limit').send_keys('2,500 Backlinks')
    driver.find_element(By.ID, 'button').click()
    time.sleep(5)
    driver.switch_to.new_window('tab')
    e2 = driver.current_window_handle
    e.append(e2)
    driver.get('https://autobacklinkbuilder.com/freebacklinks/links.php')
    time.sleep(3)
    driver.find_element(By.ID, 'url').send_keys('www.oxnrich.com')
    driver.find_element(By.ID, 'keyword').send_keys('oxnrich')
    driver.find_element(By.ID, 'limit').send_keys('2,500 Backlinks')
    driver.find_element(By.ID, 'button').click()
    time.sleep(5)
    driver.switch_to.new_window('tab')
    e3 = driver.current_window_handle
    e.append(e3)
    driver.get('https://autobacklinkbuilder.com/freebacklinks/links.php')
    time.sleep(3)
    driver.find_element(By.ID, 'url').send_keys('www.oxnrich.com')
    driver.find_element(By.ID, 'keyword').send_keys('oxnrich')
    driver.find_element(By.ID, 'limit').send_keys('2,500 Backlinks')
    driver.find_element(By.ID, 'button').click()
    time.sleep(5)
    global i
    i = 1
    print(i)
    reset(i)

def reset(i):
    for x in e:
        driver.switch_to.window(x)
        time.sleep(5)
        driver.find_element(By.ID, 'button').click()
    i+= 1
    loop(i)

def loop(i):
    for x in e:
        driver.switch_to.window(x)
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
   print("call default function")
   go()