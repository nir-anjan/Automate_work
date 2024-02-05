import pyautogui
import time
import contacts

def find_more():
    x,y=0,0
    print("finding_more")
    while True :
        if(x==0):
            try:
                x,y=pyautogui.locateCenterOnScreen("./image/more.png",confidence=0.8)
                return x,y
            except:
                print("connet not found in more")
        else:
            return x,y
        
def find_connect():
    x,y=0,0
    print("finding connect button")
    while True :
        if(x==0):
            try:
                x,y=pyautogui.locateCenterOnScreen("./image/connect1.png")
                return x,y
            except:
                print("connect1 not found in page")
                try:
                    x,y=pyautogui.locateCenterOnScreen("./image/connect2.png")
                    return x,y
                except:
                    print("connect2 not found in page")
                    try:
                        x,y=pyautogui.locateCenterOnScreen("./image/connect3.png")
                        return x,y
                    except:
                        print("connect3 (in more button) not found in page")
                        return x,y
        else:
            return x,y
        

def find_send_without_note():
    x,y=0,0
    print("_send_without_note")
    while True :
        if(x==0):
            try:
                x,y=pyautogui.locateCenterOnScreen("./image/send_without_note.png",confidence=0.8)
                return x,y
            except:
                print("send_without_note button not found ")
        else:
            return x,y


def find_sent_req():
    x,y=0,0
    print("_sent_req")
    while True :
        if(x==0):
            try:
                x,y=pyautogui.locateCenterOnScreen("./image/sent_req.png",confidence=0.8)
                return x,y
            except:
                print("sent_req  not found ")
                try:
                    x,y=pyautogui.locateCenterOnScreen("./image/sent_req_n.png",confidence=0.8)
                    return x,y
                except:
                    print("sent_req  not found ")
                    try:
                        x,y=pyautogui.locateCenterOnScreen("./image/undefined.png",confidence=0.8)
                        return x,y
                    except:
                        print("undefined  not found ")
        else:
            return x,y

def find_extracting_contacts():
    x,y=0,0
    print("extracting_contacts")
    while True :
        if(x==0):
            try:
                x,y=pyautogui.locateCenterOnScreen("./image/extracting_contacts.png",confidence=0.8)
                return x,y
            except:
                print("extracting_contacts  not found ")
    

def connect():
    time.sleep(2)
    a,b=find_extracting_contacts()
    print(a,b)
    if(a):
        
        q,w=find_sent_req()
        if(q):
            pyautogui.click()
            try:
                x1,y1=find_connect()
                if(x1):
                    pyautogui.moveTo(x1,y1)
                    pyautogui.click(x1,y1)
                    time.sleep(2)
                    x2,y2=find_send_without_note()
                    if(x2):
                        pyautogui.moveTo(x2,y2)
                        pyautogui.click(x2,y2)
                        print("connection sent")
                    else:
                        print("sent without a note button not found")
                else:
                    x1,y1=find_more()
                    if(x1):
                        pyautogui.moveTo(x1,y1)
                        pyautogui.click(x1,y1)
                        time.sleep(2)
                        x2,y2=find_connect()
                        if(x2):
                            pyautogui.moveTo(x2,y2)
                            pyautogui.click(x2,y2)
                            time.sleep(2)
                        x3,y3=find_send_without_note()
                        if(x3):
                            pyautogui.moveTo(x3,y3)
                            pyautogui.click(x3,y3)
                            print("connection sent")
                        else:
                            print("sent without a note button not found")
                    else:
                        print("more not found")
            except:
                print("connecton not send error ")
    
        


    return


# time.sleep(3)
# contacts.contact_scan()
# connect()