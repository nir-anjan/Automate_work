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


"""
This Python script employs a while loop to execute various functions based on responses. It begins by sleeping for 2 seconds,
then enters the loop, invoking click_link() from link_and_about_functions. On "success," it prints a success message and proceeds 
with post scanning, scrolling, contact scanning, and connection sending. The loop breaks after successfully sending connection 
requests five times (count==5)
"""

#main
time.sleep(2)
count=0
while True:
    resp=0 
    resp=link_and_about_functions.click_link()
    
    time.sleep(2)
    if( resp):

        print_speak("success confirmed, continuing with the profile")
        post_functions.post_scan()
        time.sleep(2)
        pyautogui.moveTo(905,469)
        pyautogui.scroll(1000)
        contacts.contact_scan()
        #print("1")
        send_connections.connect()
        #print("2")
        count+=1
        print_speak("connection sent "+ str(count))

        time.sleep(1)
        #break
    elif(resp==2):
        print("waiting for page to load again")
    elif(resp==-1):
        break
    elif(testfor_linkerror.check_fault_link()):
        testfor_linkerror.fault_link()

    if(count==30):
        print_speak("all "+str(count)+" connections have been  sent successfully")
        break
  
