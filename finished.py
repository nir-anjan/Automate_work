import pyautogui
import time


def check_skip():
    try:
        x,y=0,0
        x,y=pyautogui.locateCenterOnScreen("skip.png")
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
        x,y=pyautogui.locateCenterOnScreen("success.png")
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
            x,y=pyautogui.locateCenterOnScreen("extracting_about.png")
            print("Waiting for extracting_about")
    except:
        try:
            while True:
                time.sleep(1)
                x,y=pyautogui.locateCenterOnScreen("submitting.png")
                print("Waiting for submitting")
        except:
            return

def click_link(): #success|
    try:
        x,y=pyautogui.locateCenterOnScreen("link.png")
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        print("clicked on link:- click_link()")
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
       
        return 
    except:
        print("error Link not found")
        return "error"


