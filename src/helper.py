from pyautogui import *
import pyautogui
import time
import random

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

def down(anchor):
    image=pyautogui.locateOnScreen(anchor,confidence=0.8)
    #Puts the cursor to the left of the highest buy button
    x = image.left-image.width
    y = image.top+image.height/2
    
    pyautogui.moveTo(x,y)
    #Scrolls
    pyautogui.scroll(-400,x=x,y=y)
    time.sleep(.5)

def check(name):
    try:
        location = pyautogui.locateOnScreen(name,confidence=0.8)
        return location
    except:
        print('Cannot find')
        return None
