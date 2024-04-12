import pyautogui as p
import time
import random as r

# Constants
PROFILE_DELAY = 2 # for slow internet connection set 4 else set 2
SCROLL_DELAY = 2
TAB_CLOSE_DELAY = 1
VIDEO_PLAY_TIME = 48

accountCoordinates = [(1570, 573), (1574, 700), (1584, 828), (1624, 986), (1578, 326), (1557, 460), (1612, 601), (1588, 714), (1590, 840)]
profileCoordinates = [(834,439), (1082,453),(1278,477)]
# profileCoordinates = [(834,439), (1082,453),(1278,477),(635,689)]

# Global Variables
counter = 1 # counter to keep track of accounts

# Change Account
def changeAccount(x,y):

    global counter

    # click on profile icon
    p.moveTo(1845,174,2)
    time.sleep(PROFILE_DELAY) 
    p.click()

    # click on switch account button
    p.moveTo(1659,364,2)  
    time.sleep(PROFILE_DELAY)
    p.click()

    # scroll down
    if(counter >= 5 and counter < 10): # scroll down after 5 accounts
        time.sleep(SCROLL_DELAY)
        p.scroll(-1000) # scroll down
        time.sleep(SCROLL_DELAY)
 
    # choose next account
    p.moveTo(x,y,2)
    p.click()
    counter += 1


def runVideo(url):

    # opening new tab and closing previous tab
    p.moveTo(327,22,2) # open new tab
    p.click()

    p.moveTo(288,22) # close previous tab
    time.sleep(TAB_CLOSE_DELAY)
    p.click()
    time.sleep(TAB_CLOSE_DELAY)
    
    # search for youtube video
    p.moveTo(479,74,2) 
    p.typewrite('')
    p.typewrite(url)
    p.press("enter")


    # For Brave Browser no need to click on video to play but for Chrome it is required, so configure accordingly 
    """
    time.sleep(4)   
    p.moveTo(704,536,2) # mouse position to click on video in 2 seconds
    p.click()
    """

    # time period for video to play
    time.sleep(VIDEO_PLAY_TIME) 


# function to open first profile in chrome and search for youtube video
def openProfile(x,y,videos):

    # open Profile 1 in Chrome
    p.moveTo(x,y,2)
    p.click()

    for key,value in accountCoordinates:

        # random selection of youtube video
        url = r.choice(videos)

        runVideo(url)

        changeAccount(key,value) # change account to next account


# main body of code

# For single video task put same video link in list


# For multiple videos task put all video links in list


# for testing purpose only 6 videos are added
testVideos = [
    "https://youtu.be/-yxFU2b3U6U?si=11Hnl5lB5tLbaxnJ",
    "https://youtu.be/90uOlwRuWZw?si=tdPf45dlliI4A09u",
    "https://www.youtube.com/watch?v=_O7jIYf5edU",
    "https://www.youtube.com/watch?v=sFJ0O8C99nE",
    "https://www.youtube.com/watch?v=VAQRCCWsi-s",
    "https://youtu.be/P5bOIKpT6_A?si=UFIkH7QWaHoiEhia"
]

# automatically getting profile coordinates from list and looping the process for all profiles

for key,value in profileCoordinates:

    # open chrome application
    p.moveTo(46,282,2)
    p.doubleClick()
    
    openProfile(key,value,testVideos
                ) 

    time.sleep(VIDEO_PLAY_TIME)

    changeAccount(1570,573) # change account to 1st account

    
    # set counter value back to 1 for next profile
    counter = 1

    # closing chrome application
    p.moveTo(284,22,2)
    p.click()
    