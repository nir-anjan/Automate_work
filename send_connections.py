import pyautogui
import time
import contacts


"""
find_more()

Description:
This Python function, find_more(), utilizes PyAutoGUI to locate the center of an image on the screen, specifically 
the "./image/more.png" image. The function is designed to run indefinitely in a while loop, attempting to find the image. 
If the image is found, it returns the x, y coordinates of the center of the located image. If the image is not found, an 
exception is caught, and the function prints "connet not found in more" to the console, setting x, y coordinates to 0 before 
returning them.

Note: PyAutoGUI and the specified image file are assumed to be available for the function to run successfully.

"""
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
        


"""
find_connect()

Description:
This Python function, find_connect(), uses PyAutoGUI to locate the center of different images on the screen, 
representing a "Connect" button. The images to be located are "./image/connect1.png", "./image/connect2.png", 
and "./image/connect3.png". The function is designed to run indefinitely in a while loop, attempting to find each 
image in sequence. If any of the images are found, it returns the x, y coordinates of the center of the located image. 
If none of the images are found, the function prints corresponding error messages to the console and sets x, y coordinates 
to 0 before returning them.

Note: PyAutoGUI and the specified image files are assumed to be available for the function to run successfully.

"""      
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
        

"""
find_send_without_note.py

Description:
This Python function, find_send_without_note(), uses PyAutoGUI to locate the center of an image on the screen, 
specifically the "./image/send_without_note.png" image. The function is designed to run indefinitely in a while loop, 
attempting to find the image. If the image is found, it returns the x, y coordinates of the center of the located image. 
If the image is not found, an exception is caught, and the function prints "send_without_note button not found" to the console, 
setting x, y coordinates to 0 before returning them.

Note: PyAutoGUI and the specified image file are assumed to be available for the function to run successfully.

"""

def find_send_without_note():
    x,y=0,0
    print("_send_without_note")
    c=0
    while True :
        if(x==0):
            try:
                x,y=pyautogui.locateCenterOnScreen("./image/send_without_note.png",confidence=0.8)
                return x,y
            except:
                print("send_without_note button not found ")
                c+=1
                if(c==3):
                    return x,y
                   

        else:
            return x,y




"""

"""

def find_send_button():
    x,y=0,0
    print("_send_button")
    c=0
    while True :
        if(x==0):
            try:
                x,y=pyautogui.locateCenterOnScreen("./image/send_button.png",confidence=0.8)
                return x,y
            except:
                print("send button not found ")
                c+=1
                if(c==3):
                    return x,y
                   

        else:
            return x,y

"""
find_sent_req()

Description:
This Python function, find_sent_req(), uses PyAutoGUI to locate the center of different images on the screen, representing 
a "Sent Request" button. The images to be located are "./image/sent_req.png", "./image/sent_req_n.png", and "./image/undefined.png". 
The function is designed to run indefinitely in a while loop, attempting to find each image in sequence. If any of the images are 
found, it returns the x, y coordinates of the center of the located image. If none of the images are found, the function prints 
corresponding error messages to the console and sets x, y coordinates to 0 before returning them.

Note: PyAutoGUI and the specified image files are assumed to be available for the function to run successfully.


"""

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
        

"""
find_extracting_contacts()

Description:
This Python function, find_extracting_contacts(), uses PyAutoGUI to locate the center of an image on the screen, specifically 
the "./image/extracting_contacts.png" image. The function is designed to run indefinitely in a while loop, attempting to find 
the image. If the image is found, it returns the x, y coordinates of the center of the located image. If the image is not found, 
an exception is caught, and the function prints "extracting_contacts not found" to the console, setting x, y coordinates to 0 before 
returning them.

Note: PyAutoGUI and the specified image file are assumed to be available for the function to run successfully.

"""

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

    
"""
connect.py

Description:
This Python function, connect(), performs a series of actions to send a connection request on a platform. 
It includes a 2-second sleep and calls the find_extracting_contacts() function to locate the "Extracting Contacts" 
button. If found, it prints the x, y coordinates and proceeds to call find_sent_req() to check for a "Sent Request" button. 
If found, it clicks on the screen and attempts to find the "Connect" button. If found, it clicks on the "Connect" button and then 
looks for the "Send without a note" button. If found, it clicks on the "Send without a note" button, printing "Connection sent" 
to the console. If any of the buttons are not found, it prints corresponding error messages.

Note: PyAutoGUI and the specified image files are assumed to be available for the function to run successfully.

"""

def connect():
    time.sleep(2)
    a,b=find_extracting_contacts()
    #print(a,b)
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
                        
                        x3,y3=find_send_button()
                        if(x3):
                            pyautogui.moveTo(x3,y3)
                            pyautogui.click(x3,y3)
                            print("connection sent")
                        else:
                            print("sent button not found")
                            
                        #print("sent without a note button not found")
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
                            x3,y3=find_send_button()
                            if(x3):
                                pyautogui.moveTo(x3,y3)
                                pyautogui.click(x3,y3)
                                print("connection sent")
                            else:
                                print("sent button not found")
                    else:
                        print("more not found")
            except:
                print("connecton not send error ")

    return


# time.sleep(3)
# contacts.contact_scan()
# connect()