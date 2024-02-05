import pyautogui
import time


def check_skip():
    try:
        x,y=0,0
        #time.sleep(2)                     #add if success not found or put a confidence of 0.8
        x,y=pyautogui.locateCenterOnScreen("./image/skip.png")
        print("skip found")
        return x
    except:
        x=0
        print("skip not found")
        #exit()
        return x
    
def check_success():
    try:
        x,y=0,0
        #time.sleep(2)                    #add if success not found or put a confidence of 0.8
        x,y=pyautogui.locateCenterOnScreen("./image/success.png")
        print("success not found")
        return x
    except:
        x=0
        print("success not found")
        #exit()
        return x 

def wait_untill():
    try:
        while True:
            time.sleep(5)
            x,y=pyautogui.locateCenterOnScreen("./image/extracting_about.png",confidence=0.8)
            print("Waiting for extracting_about")
    except:
        try:
            while True:
                time.sleep(1)
                x,y=pyautogui.locateCenterOnScreen("./image/submitting.png",confidence=0.8)
                print("Waiting for submitting")
        except:
            return

def click_link(): #success|clicked|error
    try:
        x,y=pyautogui.locateCenterOnScreen("./image/link.png",confidence=0.8)
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        print("clicked on link:- click_link()")
        #time.sleep(6)
        pyautogui.moveTo(1668,308,1)
        pyautogui.click(1668,308)
        print("clicked on link ")
        time.sleep(5)
        wait_untill()
        if(check_skip()):
            click_link()
            
            return "clicked"
        elif(check_success()):
            return "success"
        else:
            time.sleep(10)
        return 
    except:
        print("error Link not found")
        return "error"


