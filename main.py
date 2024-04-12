import pyautogui as p
import time

counter = 1
# Change Account
def changeAccount(x,y):
    # click on profile icon
    p.moveTo(1846,194,2)
    p.click()

    # click on switch account button
    p.moveTo(1563,398,2)  
    p.click()

    global counter

    # scroll down
    if(counter >= 5 and counter < 10):
        time.sleep(2)
        p.scroll(-1000)
        time.sleep(2)
 
    # choose next account
    p.moveTo(x,y,2)
    p.click()
    counter += 1

def subscribe():
    # click on subscribe button
    time.sleep(4)
    p.moveTo(1731,367,2)
    p.click()

def openChrome(x,y):
    # Open Chrome
    p.moveTo(49,267,2)
    p.doubleClick()

    # open Profile 1
    p.moveTo(x,y,2)
    p.doubleClick()

    # open Youtube
    p.moveTo(744,643,2)
    p.click()
    
    # search for youtube
    p.moveTo(684,187,2) 
    time.sleep(4)
    p.click()
    p.typewrite("Dhruv Rathee")
    p.press("enter")

# First Profile
def pro():
    # click on subscribe button and move to next account 
    subscribe()
    changeAccount(1567,584) # 2nd account
    subscribe()
    changeAccount(1571,708) # 3rd account
    subscribe()
    changeAccount(1559,832) # 4nd account
    subscribe()
    changeAccount(1593,976) # 5th account
    subscribe()

    changeAccount(1590,299) # 6th account
    subscribe()
    changeAccount(1559,445) # 7nd account
    subscribe()
    changeAccount(1593,580) # 8nd account
    subscribe()
    changeAccount(1497,705) # 9nd account
    subscribe()
    changeAccount(1590,832) # 10th account
    subscribe()

    # change account to 1st account
    changeAccount(1567,584)

    # close chrome
    p.moveTo(321,24,2)
    p.click()



# take cursor mouse position
# time.sleep(5)
# print(p.position())

# open chrome
openChrome(1036,461)
pro()
openChrome(1275,463)
pro()