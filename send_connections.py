import pyautogui
import time


def find_connect_in_more():
    x,y=0,0
    while True :
        if(x==0):
            try:
                x,y=pyautogui.locateCenterOnScreen("./image/.png",confidence=0.8)
            except:
                print("connet not found in more")
        else:
            return x,y
        
def find_connect():
    x,y=0,0
    while True :
        if(x==0):
            try:
                x,y=pyautogui.locateCenterOnScreen("./image/connet1.png")
            except:
                print("connect1 not found in page")
                try:
                    x,y=pyautogui.locateCenterOnScreen("./image/connet2.png")
                except:
                    print("connect2 not found in page")
        else:
            return x,y