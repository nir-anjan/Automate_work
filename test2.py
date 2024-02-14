import pyautogui
import time
import link_and_about_functions #functions for click link with condition 
import post_functions   #functions for post section
import contacts         #function for contactions 
import testfor_linkerror    #function for page not found 
import send_connections



import pyttsx3
engine = pyttsx3.init()


def print_speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    print(text)
    engine.runAndWait()
    return


time.sleep(2)

while True:
    resp=0 
    aa =testfor_linkerror.fault_link()
    if(aa):
        bb=testfor_linkerror()

    print_speak("skip found, loading next profile " )
    x,y=pyautogui.locateCenterOnScreen("./image/link.png",confidence=0.8)
    pyautogui.moveTo(x,y)
    pyautogui.click(x,y)
    print("clicked on link button")

    #time.sleep(6)
    pyautogui.moveTo(1668,308,3)
    pyautogui.click(1668,308)
    print("clicked on link ")
    
    link_and_about_functions.wait_untill() 
    time.sleep(5)
    if(link_and_about_functions.check_skip()):
        
        print_speak("skip found, loading next profile " )
        x,y=pyautogui.locateCenterOnScreen("./image/link.png",confidence=0.8)
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        print("clicked on link button")
        #time.sleep(6)
        pyautogui.moveTo(1668,308,3)
        pyautogui.click(1668,308)
        print("clicked on link ")
        continue
    elif(link_and_about_functions.check_success_2()):
        print_speak("SUCCESS " )
        print_speak("success confirmed, continuing with the profile")
        post_functions.post_scan()
        time.sleep(2)
        pyautogui.moveTo(905,469)
        pyautogui.scroll(1000)
        contacts.contact_scan()
        #print("1")
        send_connections.connect()
        #print("2")
        
        print_speak("connection sent ")

        time.sleep(1)
        break
            
    else:
        time.sleep(5)  #for loading
            
    

'''

time.sleep(2)
post_functions.post_scan()
time.sleep(2)
pyautogui.moveTo(905,469)
pyautogui.scroll(1000)
contacts.contact_scan()
#print("1")
send_connections.connect()
print("2")
#count+=1
time.sleep(1)
#break 
'''