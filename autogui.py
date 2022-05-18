import pyautogui
import os
import time

def press_fun(key):
    pyautogui.press(key)

def type_fun(val):
    pyautogui.typewrite(val)

os.startfile("chrome.exe")
time.sleep(5)
text = "python"
type_fun(text)
time.sleep(5)

press_fun("enter")
time.sleep(5)
pyautogui.hotkey('ctrl','w')