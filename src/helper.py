from pyautogui import *
import pyautogui
import time
import random
import keyboard

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
    print('Moving down')
    image=check(anchor)
    image = pyautogui.center(image)
    rand_x = random.randrange(-60, 60)
    rand_y = random.randrange(-15, 15)
    if (image == None):
        return
    #Puts the cursor to the left of the highest buy button
    x = image.x+rand_x
    y = image.y+rand_y
    pyautogui.moveTo(x,y)

    #Scrolls
    pyautogui.scroll(-400,x=x,y=y)
    time.sleep(1)

def check(name):
    try:
        location = pyautogui.locateOnScreen(name,confidence=0.8)
        print('Found: ',location)
        return location
    except:
        print('Cannot find ',name)
        return None
    
def exit_check():
    if (keyboard.is_pressed('q') == True):
        print('Exit flag triggered')
        return True
    else:
        return False