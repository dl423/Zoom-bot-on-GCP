import subprocess
import os
import pyautogui
import time
from datetime import datetime

def locate_click(img):
    location = pyautogui.locateCenterOnScreen(img)
    if location == None:
        print(img, "not detected!")
        return -1
    pyautogui.moveTo(location)
    pyautogui.click()
    print("Detected and clicked according to", img)
    return 0

def locate_all_click(img):
    location = pyautogui.locateAllOnScreen(img)
    if location == None:
        print(img, "not detected!")
        return -1
    for loc in location:
        pyautogui.moveTo(loc)
        pyautogui.click()
        print("Detected and clicked according to", img)
    return 0


def join_zoom_room(meetingid, pswd):
    print("join_zoom_room(m_id, m_pswd) started")
    
    #If on windows use below line for opening zoom
    os.startfile(r"C:\Users\dl\AppData\Roaming\Zoom\bin\Zoom.exe")
    
    #If on mac / Linux use below for opening zoom
    #subprocess.call(["/usr/bin/open", "/Applications/zoom.us.app"])

    time.sleep(10)
    locate_click('version_text.png')
    ret = locate_click('join_button.png')
    if ret == -1:
        ret = locate_click('join_button2.png')
        if ret == -1:
            pyautogui.press('enter')
    time.sleep(4)
    pyautogui.write(meetingid)

    # Disables both the camera and the mic
    locate_all_click('media_btn.png')
    locate_click('join_btn.png')
    time.sleep(3)
    pyautogui.write(pswd)
    pyautogui.press('enter')

    print("join_zoom_room(m_id, m_pswd) completed\n")
    return

def share_screen_start():
    print("share_screen_start() started")
    time.sleep(3)
    pyautogui.hotkey('alt', 'S')
    time.sleep(1)
    locate_all_click('media_btn.png')
    time.sleep(2)
    locate_click('share_btn.png')
    time.sleep(10)
    print("share_screen_start() completed\n")
    return

def share_screen_end():
    print("share_screen_end() started")
    time.sleep(1)
    pyautogui.moveTo(1, 1)
    pyautogui.moveTo(100, 100)
    time.sleep(2)
    locate_click('stop_share_btn.png')
    print("share_screen_end() completed\n")
    return

def leave_meeting():
    print("leave_meeting() started")
    time.sleep(2)
    pyautogui.hotkey('alt', 'q')
    pyautogui.press('enter')
    print("leave_meeting() completed\n")
    return

def play_video(video, duration):
    print("play_video() started")
    time.sleep(1)
    os.startfile(video)
    time.sleep(3)
    pyautogui.hotkey('alt', 'enter')
    time.sleep(duration)
    pyautogui.hotkey('alt', 'enter')
    time.sleep(1)
    pyautogui.hotkey('alt', 'f4')
    print("play_video() completed")

time.sleep(5)
os.chdir(r"C:\Users\dluo567\Documents\Zoom-Automation-Python-master")

# replace the room id and password here
m_id = "123456789"
m_pswd = "Pwd"

# sequence of videos to be played
video = [r"C:\Users\dl\Desktop\video1.mp4", r"C:\Users\dl\Desktop\video2.mp4", r"C:\Users\dl\Desktop\video3.mp4"]

# main code
join_zoom_room(m_id, m_pswd)
share_screen_start()
for i in range(10):
    play_video(video[i], 175)
share_screen_end()
leave_meeting()
