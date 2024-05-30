import helper
from pyautogui import *
import pyautogui
import datetime
import keyboard
import sys
import time

click = helper.click
check = helper.check
down = helper.down

def battle_sequence(battle):
    click(battle)
    start_battle_button = check('assets/arena/start_battle.png')
    click(start_battle_button)
    
    while(check('assets/arena/auto.png') == None):
        click(start_battle_button)
        time.sleep(.2)
    
    click(check('assets/arena/auto.png'))
    victory = check('assets/arena/confirm_victory.png')
    click(victory)
    

#Program begins
debug_timer = 2
exit_flag = 0
time.sleep(2) #wait 2 seconds in case user needs to click into bluestacks

timeout = 5 #if program hangs for 5 seconds, terminate
print("Starting Program")

while ((exit_flag == 0)):
    #Locate fight button
    battle = check('assets/arena/fight_button.png')

    if (battle == None):
        down()
    else:
        click(battle)
    
