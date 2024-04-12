import pyautogui as p
import time
import random as r

# Constants
SCROLL_DELAY = 2
VIDEO_PLAY_TIME = 5
TAB_SWITCH_DELAY = 2
TAB_CLOSE_DELAY = 2
PROFILE_COUNT = 2
ACCOUNT_COUNT = 9

# Functions
def change_account(x, y):
    global counter

    p.moveTo(1845, 174, 2)  # Click on profile icon
    time.sleep(4)  # Adjust sleep based on internet speed
    p.click()

    p.moveTo(1659, 364, 2)  # Click on switch account button
    time.sleep(4)
    p.click()

    if ACCOUNT_COUNT <= counter < ACCOUNT_COUNT * 2:
        time.sleep(SCROLL_DELAY)
        p.scroll(-1000)  # Scroll down
        time.sleep(SCROLL_DELAY)

    p.moveTo(x, y, 2)  # Choose next account
    p.click()
    counter += 1

def run_video(url):
    p.moveTo(327, 22, 2)  # Open new tab
    p.click()

    p.moveTo(288, 22)  # Close previous tab
    time.sleep(TAB_CLOSE_DELAY)
    p.click()
    time.sleep(TAB_CLOSE_DELAY)

    p.moveTo(479, 74, 2)  # Search for YouTube video
    p.typewrite('')
    p.typewrite(url)
    p.press("enter")

    time.sleep(VIDEO_PLAY_TIME)

def open_profile(x, y, videos):
    p.moveTo(x, y, 2)  # Open profile in Chrome
    p.doubleClick()

    account_coordinates = [(1570, 573), (1574, 700), (1584, 828), (1624, 986),
                           (1578, 326), (1557, 460), (1612, 601), (1588, 714), (1590, 840)]

    for key, value in account_coordinates:
        url = r.choice(videos)
        run_video(url)
        change_account(key, value)

# Main body
videos = [
    "https://youtu.be/-yxFU2b3U6U?si=11Hnl5lB5tLbaxnJ",
    "https://youtu.be/90uOlwRuWZw?si=tdPf45dlliI4A09u",
    "https://www.youtube.com/watch?v=_O7jIYf5edU",
    "https://www.youtube.com/watch?v=sFJ0O8C99nE",
    "https://www.youtube.com/watch?v=VAQRCCWsi-s",
    "https://youtu.be/P5bOIKpT6_A?si=UFIkH7QWaHoiEhia"
]

profile_coordinates = [(834, 439), (1082, 453)]

for key, value in profile_coordinates:
    p.moveTo(46, 282, 2)  # Open Chrome application
    p.doubleClick()

    open_profile(key, value, videos)

    counter = 0
    change_account(1570, 573)  # Change account to 1st account

    print('Profile completed:', counter)

    p.moveTo(284, 22, 2)  # Close Chrome
    p.click()

    time.sleep(TAB_CLOSE_DELAY)
    p.click()
