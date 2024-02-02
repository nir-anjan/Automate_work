import pyautogui
import time
import finished

def check_fault_link():
    while True:
        try:
            x,y=0,0
            x,y=pyautogui.locateCenterOnScreen("./image/page_not_exist.png")
            return x
        except:
            x=0
            print("page not found")
            #exit()
            return x
    
def fault_link():
    while True:
        x=0
        try:
            x,y=pyautogui.locateCenterOnScreen("./image/page_not_exist.png",confidence=0.8)
        except:
            print("page_not_exist not present ")
        if(x):
            x,y=pyautogui.locateCenterOnScreen("./image/people_list.png")
            pyautogui.click(x,y)
            print("clicked on people_lists")
            try:
                x,y=pyautogui.locateCenterOnScreen("./image/link.png",confidence=0.8)
                pyautogui.moveTo(x,y)
                pyautogui.click(x,y)
                pyautogui.moveTo(1668,308,1)
                pyautogui.click(1668,308)
                print("clicked on link")
                
                res=check_fault_link()
                if(res):
                    time.sleep(2)
                    fault_link()
                    time.sleep(2)
            except:
                print("e")
        else:
            return


time.sleep(3)
fault_link()