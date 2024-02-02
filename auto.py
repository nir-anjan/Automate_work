import pyautogui
import time

def find_contact():
    x,y=0,0
    while True :
        if(x==0):
            try:
                x,y=pyautogui.locateCenterOnScreen("./image/contact.png",confidence=0.8)
            except:
                print("contact not found in page")
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


def contact_scan():
    time.sleep(3)
    x,y=find_contact()
    if(x):
        pyautogui.moveTo(x,y)
        pyautogui.click()
        print("clicked:- contact info")

    time.sleep(10)
    return








"""
pyautogui.click()
    x,y=find_connect()
    if(x):
        pyautogui.moveTo(x,y)
        pyautogui.click()
        print("clicked:- connect")
    return
"""
'''
count=0
while True:
    print(pyautogui.position())
    time.sleep(2)
    count+=1
    if count==10 :
        break
        '''

