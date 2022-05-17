import pyautogui
import os
import time

def press_fun(key):
    pyautogui.press(key)

def type_fun(val):
    pyautogui.typewrite(val)

os.startfile("Notepad.exe")
time.sleep(5)

type_fun("I love Python automation")
press_fun("alt")
press_fun("f")
press_fun("s")
time.sleep(5)

type_fun(os.getcwd() + "\\" + "demgeui.txt")
time.sleep(8)
press_fun("enter")
time.sleep(2)
press_fun("alt")
press_fun("f")
press_fun("x")
