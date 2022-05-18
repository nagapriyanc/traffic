import pyautogui as py
import os
import time

os.startfile("chrome.exe")
time.sleep(12)
py.click(1174,133)
time.sleep(10)

list = ['nagapriyan.c1@gmail.com']*500

for x in list:
    py.click(102,171)
    time.sleep(2)
    py.click(825,313)
    py.typewrite(x)
    time.sleep(2)
    py.click(818,355)
    sub = 'hi good evening'
    py.typewrite(sub)
    time.sleep(2)
    py.click(957,463)
    msg = 'test '
    py.typewrite(msg)
    time.sleep(2)
    py.click(837,691)
    time.sleep(2)

