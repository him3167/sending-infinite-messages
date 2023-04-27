#first install pyautogui in cmd terminal using command
    # pip install pyautogui


import pyautogui as pg
import time 
time.sleep(5)
for i in range(100):
    pg.write('pick up the damn call')
    pg.press('enter')
    
