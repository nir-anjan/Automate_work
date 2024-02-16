import pyautogui
import time


import pyttsx3
engine = pyttsx3.init()


def print_speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    print(text)
    engine.runAndWait()
    return

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



def wait_untill():
    c=0
    try:
        while True:
            time.sleep(2)
            c+=1
            x,y=pyautogui.locateCenterOnScreen("./image/pic1.png",confidence=0.8)
            print("Waiting for pic1")

            if (x):
                a=100/0
    except:
        try:
            while True:
                time.sleep(1)
                x,y=pyautogui.locateCenterOnScreen("./image/extracting_about.png",confidence=0.8)
                print("extrating")
                if (x):
                    a=100/0
        except:
            try:
                while True:
                    time.sleep(1)
                    x,y=pyautogui.locateCenterOnScreen("./image/submitting.png",confidence=0.8)
                    print("Waiting for submitting")
                    if (x):
                        a=100/0
            except:
                return


def wait_untill_new():
    #print("this is wait untill new")
    time.sleep(2)
    while True: 
        #print("in while")
        try:
           # print("in try")
            while True:
                #print("in try while")
                time.sleep(2)
                x,y=pyautogui.locateCenterOnScreen("./image/pic1.png",confidence=0.8)
                print(x,y,"Waiting for pic1")
        except:
            try:
                while True:
                    time.sleep(1)
                    x,y=pyautogui.locateCenterOnScreen("./image/extracting_about.png",confidence=0.8)
                    print("extrating")   
            except:
                try:
                    while True:
                        time.sleep(1)
                        x,y=pyautogui.locateCenterOnScreen("./image/submitting.png",confidence=0.8)
                        print("Waiting for submitting")
                        
                except:
                    return


def click_on_link(): 
    while True:
        try:
            x,y=pyautogui.locateCenterOnScreen("./image/link.png",confidence=0.8)
            pyautogui.moveTo(x,y)
            pyautogui.click(x,y)
            print("clicked on link button")
            x,y=0,0
            while True:
                try:
                    x,y=pyautogui.locateCenterOnScreen("./image/blank.png",confidence=0.8)
                    #print(x,y)
                    
                except:
                    try:
                        x,y=pyautogui.locateCenterOnScreen("./image/getting_link.png",confidence=0.8)
                        #print(x,y)
                        
                    except:
                        #print(x,y)
                        break   #code for no link
            time.sleep(1)
            pyautogui.moveTo(1668,308,1)
            pyautogui.click(1668,308)
            print("clicked on link ")
            wait_untill_new()
            #print("leave")
            return
        except:
            return
    return



def click_link(): #success|clicked|error
    try:
        skip_count=0
        success_count=0
        while True:
            x,y=pyautogui.locateCenterOnScreen("./image/link.png",confidence=0.8)
            pyautogui.moveTo(x,y)
            pyautogui.click(x,y)
            print("clicked on link button")
            #time.sleep(6)

            pyautogui.moveTo(1668,308,3)
            pyautogui.click(1668,308)
            print("clicked on link ")

            time.sleep(5)
            wait_untill_new()
            time.sleep(2)


            if(check_skip()):
                skip_count+=1
                print_speak("Profile skipped , total skipped profile "+str(skip_count) )
                continue
            elif(check_success()):
                success_count+=1
                return 1
            
            else:
                time.sleep(5)  #for loading
                return 2    
    except:
        print("error ")
        return -1


