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

def buy(item):
    bought = False
    pos = None
    buy_start = time.time()
    buy_pos = check('assets/shoprefresh/buy_button.png')
    print(buy_pos.left+buy_pos.width-item.left)
    #Searches the area right of the mark for the buy
    buy_button = pyautogui.locateOnScreen('assets/shoprefresh/buy_button.png',region=(item.left,item.top,buy_pos.left+buy_pos.width-item.left,item.height))

    click(buy_button)
    confirm = check('assets/shoprefresh/confirm_button.png')
    #click(confirm)

#Program begins
debug_timer = 2
exit_flag = 0
time.sleep(2) #wait 2 seconds in case user needs to click into bluestacks

#Specify how long this program should be run for
run_timeout = float(input("How long should this macro be run for? (Enter in minutes): "))*60
start_time = time.time()
start_datetime = datetime.datetime.now()

timeout = 5 #if program hangs for 5 seconds, terminate
print("Starting Program")

#Locate refresh button
refresh = check('assets/shoprefresh.refresh_button.png')
if (refresh == None):
    quit

#Counter (will tell you how many mystics/covenants were bought at the end)
mystic_count = 0
covenant_count = 0
refresh_count = 0

while ((exit_flag == 0) and (time.time() < start_time+run_timeout)):

    cov_pos = check('assets/shoprefresh/covenant.png')
    mystic_pos = check('assets/shoprefresh/mystic.png')

    if (cov_pos != None):
        buy(cov_pos)
        covenant_count += 1
    if (mystic_pos != None):
        buy(mystic_pos)
        mystic_count += 1

    down('assets/shoprefresh/buy_button.png')

    cov_pos2 = check('assets/shoprefresh/covenant.png')
    mystic_pos2 = check('assets/shoprefresh/mystic.png')

    if (cov_pos2 != None):
        buy(cov_pos)
        covenant_count += 1
    if (mystic_pos != None):
        buy(mystic_pos)
        mystic_count += 1
    
    debug_time_start = time.time()
    while (time.time() < debug_time_start+debug_timer):
        if (keyboard.is_pressed('q') == True):
            exit_flag = 1

    if exit_flag == 1:
        break
    
    click(refresh)
    time.sleep(.3)
    timeout_start = time.time()
    while(time.time() < (timeout_start + timeout)):
        confirm_pos = check('assets/shoprefresh/confirm_button.png')
        if (keyboard.is_pressed('q') == True):
            exit_flag = 1
            break
        if (confirm_pos != None):
            #Confirm refresh
            click(confirm_pos)
            refresh_count=refresh_count+1
            break
    if exit_flag == 1:
        break

    time.sleep(0.5)
# End of script
time_ran = datetime.datetime.now()-start_datetime
time_ran_mins = round(time_ran.total_seconds()/60)

if (exit_flag == 1):
    sys.stderr.write(f'\n\nMacro has forcefully exited.\n')
else:
    sys.stderr.write(f'\n\nMacro has finished running.\n')
    
sys.stderr.write(f'Total time ran: {time_ran_mins} minutes and {time_ran.seconds % 60} seconds\n\n')
sys.stderr.write(f'Total times refreshed: {refresh_count} \nSkystones used: {refresh_count*3}\n\n')
sys.stderr.write(f'Covenant medals bought: {covenant_count*5} \nMystic medals bought: {mystic_count*50}\n\n')
sys.stderr.write(f'Total gold used: {covenant_count*184000 + mystic_count*280000}\n')