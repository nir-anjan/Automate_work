import time
import pyautogui


def check_skip():
    try:
        x,y=0,0
        time.sleep(2)                     #add if success not found or put a confidence of 0.8
        
        x,y=pyautogui.locateCenterOnScreen("./image/skip.png",confidence=0.8)
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
        time.sleep(2)                    #add if success not found or put a confidence of 0.8
        x,y=pyautogui.locateCenterOnScreen("./image/success.png",confidence=0.8)
        #x,y=pyautogui.locateCenterOnScreen("./image/success_big.png",confidence=0.8)
        print("success found")
        return x
    except:
        x=0
        print("success not found")
        #exit()
        return x 
    
def check_success_2():
    try:
        while True :
            x,y=0,0
            time.sleep(2)                    #add if success not found or put a confidence of 0.8
            try:
                
                x,y=pyautogui.locateCenterOnScreen("./image/success.png",confidence=0.8)
                print("success found")
                return x
            except:
                x,y=pyautogui.locateCenterOnScreen("./image/success_big.png",confidence=0.8)
                print("success big found")
                return x
    except:
        x=0
        print("success not found")
        #exit()
        return x 

time.sleep(2)
x=check_skip()
if(x):
    print("sndkjfhjs")