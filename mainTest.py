import pyautogui
import time
import link_and_about_functions #functions for click link with condition 
import post_functions   #functions for post section
import contacts         #function for contactions 
import testfor_linkerror    #function for page not found 
import send_connections



#main
time.sleep(2)
count=0
while True: 
    resp=link_and_about_functions.click_link()
    count+=1
    time.sleep(2)
    if( resp=="success"):
        print("code for success")
        post_functions.post_scan()
        time.sleep(2)
        pyautogui.moveTo(905,469)
        pyautogui.scroll(1000)
        contacts.contact_scan()
        send_connections.connect()
        break

    elif(testfor_linkerror.check_fault_link()):
        testfor_linkerror.fault_link()

    elif(resp=="error"):
        break


    if(count==20):
        break
  
