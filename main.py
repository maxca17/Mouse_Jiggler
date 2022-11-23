import pyautogui
import time 
import random
q = 3

def mousemove():
    while q == 3:
        x = random.randint(1,500)
        y = random.randint(1,500)
        time.sleep(30)
        pyautogui.moveTo(x, y)
        print('Mouse was moved')

mousemove()















