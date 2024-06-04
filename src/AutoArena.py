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
exit_check = helper.exit_check
def battle_sequence(battle):
    print('Starting battle sequence')
    
    click(battle)
    time.sleep(.4)
    click(battle)

    start_battle_button = None
    while(start_battle_button == None):
        start_battle_button = check('assets/arena/start_battle.png')
        time.sleep(.5)
        if (exit_check() == True):
            return
    click(start_battle_button)

    auto = None
    auto_check = None
    while(auto == None and auto_check == None):
        auto = check('assets/arena/auto.png')
        auto_check = check('assets/arena/auto_check.png')
        if (exit_check() == True):
            return
        if (auto != None):
            click(auto)
        time.sleep(1)
    
    victory = None
    while(victory == None):
        #click(start_battle_button)
        victory = check('assets/arena/confirm_victory.png')
        time.sleep(.5)
        if (exit_check() == True):
            return
    click(victory)
    

#Program begins
debug_timer = 2
exit_flag = 0
time.sleep(2) #wait 2 seconds in case user needs to click into bluestacks

timeout = 5 #if program hangs for 5 seconds, terminate
count = 0
print("Starting Program")

while ((exit_flag == 0)):
    #Locate fight button
    battle = check('assets/arena/fight_button.png')

    if (battle == None):
        count +=1;
        down('assets/arena/anchor.png')
        time.sleep(.5)
        if count > 5:
            break
    else:
        count = 0
        battle_sequence(battle)
    if (exit_check() == True):
        break

