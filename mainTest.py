import pyautogui
import time
import finished
import sys
import test  #post
import auto
import testfor_linkerror
 



#main
time.sleep(2)
count=0
while True: 
    resp=finished.click_link()
    count+=1
    time.sleep(2)
    if( resp=="success"):
        print("code for success")
        test.post_scan()
        time.sleep(2)
        pyautogui.moveTo(905,469)
        pyautogui.scroll(1000)
        auto.contact_scan()
        break
    
    elif(testfor_linkerror.check_fault_link()):
        testfor_linkerror.fault_link()

    elif(resp=="error"):
        break


    if(count==20):
        break




#post
    