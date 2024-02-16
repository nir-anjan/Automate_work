
import pyautogui
import time
import link_and_about_functions #functions for click link with condition 
import post_functions   #functions for post section
import contacts         #function for contactions 
import testfor_linkerror    #function for page not found 
import send_connections

import test_fun
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
        #time.sleep(2)                    #add if success not found or put a confidence of 0.8
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
            #time.sleep(2)                    #add if success not found or put a confidence of 0.8
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




#main
skip_count=0
success_count=0
faultLink_count=0
total=0
time.sleep(2)

while True:
    link_and_about_functions.click_on_link()
    link_and_about_functions.wait_untill_new()
    #time.sleep(5)

    if(test_fun.check_skip()):
        skip_count+=1
        print(skip_count,"  Profile Skipped")

    elif(test_fun.check_success()):
        success_count+=1
        print(success_count,"  Profile accept")

        post_functions.post_scan()
        time.sleep(2)
        pyautogui.moveTo(905,469)
        pyautogui.scroll(1000)

        contacts.contact_scan()

        send_connections.connect()
        pyautogui.moveTo(905,469)
        pyautogui.click()
        
    else:
        print("An Error occurred")
        total=skip_count+success_count

    print()
    print(" \n \nTotal Profiles checked: ",total)
    print("Total valid profiles: ",success_count)
    print("Total Invalid profiles: ",skip_count)
    print("Total Invalid links: ",faultLink_count)
    print()
    if(testfor_linkerror.check_fault_link()):
        testfor_linkerror.fault_link_2()
        faultLink_count+=1
        
   #g time.sleep(5)
    

    
    if(success_count==25):
        break
    
