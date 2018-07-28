import pygame
import time
import win32api,win32con

def run(**args):
    global username
    Songpath = "C:\Users\%s\Pictures\SLoveH.mp3" %username
    #Songpath = "D:\\files\\song\\EverythingHasChanged.mp3"
    pygame.mixer.init()
    print "[*] In Music Module"
    pygame.mixer.music.load(Songpath)
    pygame.mixer.music.play()
    for i in range(6):
        win32api.keybd_event(0xaf,0,0,0)
        win32api.keybd_event(0xaf,0,win32con.KEYEVENTF_KEYUP,0)
        time.sleep(1)
    time.sleep(300)
    return str("PLAYing...")

#run()