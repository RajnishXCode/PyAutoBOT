import pyautogui as p
import time
import random as r

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
  

# Chnaging Profiles
def pro():
    # click on takeView button and move to next account 
    time.sleep(4)
    p.moveTo(704,536,2)
    p.click()
    time.sleep(40)

    changeAccount(1567,584) # 2nd account
    time.sleep(40)
    changeAccount(1571,708) # 3rd account
    time.sleep(35)
    changeAccount(1559,832) # 4nd account
    time.sleep(43)
    changeAccount(1593,976) # 5th account
    time.sleep(46)

    changeAccount(1590,299) # 6th account
    time.sleep(35)
    changeAccount(1559,445) # 7nd account
    time.sleep(36)
    changeAccount(1593,580) # 8nd account
    time.sleep(40)
    changeAccount(1497,705) # 9nd account
    time.sleep(39)
    changeAccount(1590,832) # 10th account
    time.sleep(40)

    # change account to 1st account
    changeAccount(1567,584)

    # close chrome
    p.moveTo(321,24,2)
    p.click()



def openChrome(x,y):
    # Open Chrome application
    p.moveTo(49,267,2)
    p.doubleClick()

    # open Profile 1 in Chrome
    p.moveTo(x,y,2)
    p.doubleClick()

    url = 'https://www.youtube.com/watch?v=6n3pFFPSlW4'

    # search for youtube video
    p.moveTo(333,74,2)
    p.typewrite(url) # typing randomly selected video link in search bar
    p.press("enter")
    



# take cursor mouse position
# time.sleep(5)
# print(p.position())
    

# open chrome

# profile1
openChrome(1036,461)
pro()
openChrome(1275,463)
pro()
openChrome(1571,708)
pro()