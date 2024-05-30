from pyautogui import *
import pyautogui
import time
import datetime
import keyboard
import random
import sys
import os


def click(image):
    print('Image ',image)
    image = pyautogui.center(image)
    rand_x = random.randrange(-60, 60)
    rand_y = random.randrange(-15, 15)
    x = image.x+rand_x
    y = image.y+rand_y
    pyautogui.click(x,y)
    time.sleep(0.4)
    pyautogui.click(x,y)
def clickbuy(image):
    image.y = image.y+image.y/2
    click(image)
def down():
    image=pyautogui.locateOnScreen('assets/shoprefresh/buy_button.png',confidence=0.8)
    #Puts the cursor to the left of the highest buy button
    x = image.left-image.width
    y = image.top+image.height/2
    
    pyautogui.moveTo(x,y)
    #Scrolls
    pyautogui.scroll(-400,x=x,y=y)

def buy(item):
    bought = False
    pos = None
    buy_start = time.time() 



debug_timer = 2
exit_flag = 0
time.sleep(2) #wait 2 seconds in case user needs to click into bluestacks

#Specify how long this program should be run for
#run_timeout = float(input("How long should this macro be run for? (Enter in minutes): "))*60
#start_time = time.time()
#start_datetime = datetime.datetime.now()

try:
    print('w')
    spot = pyautogui.locateOnScreen('assets/shoprefresh/mystic.png',confidence=0.8)
    print(spot)
    a = pyautogui.locateOnScreen('assets/shoprefresh/Buy_button_Mystic.png',confidence=0.8)
    pyautogui.moveTo(a)
    click(a)
except:
    print('fail')
#down()