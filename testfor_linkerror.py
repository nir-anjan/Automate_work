import pyautogui
import time
import link_and_about_functions

"""
def check_fault_link(): Description:

This Python script uses the PyAutoGUI library to locate the center of an image on the screen. 
The image to be located is specified as "./image/page_not_exist.png". 
The script is designed to run indefinitely in a while loop, attempting to find the image on the screen. 
If the image is found, the script returns the x-coordinate of the center of the located image. 
If the image is not found, an exception is caught, and the script prints "page not found" to the console, 
setting the x-coordinate to 0 before returning it.

Note: PyAutoGUI and the specified image file are assumed to be available for the script to run successfully.

"""

def check_fault_link():
    while True:
        try:
            x,y=0,0
            x,y=pyautogui.locateCenterOnScreen("./image/page_not_exist.png")
            return x
        except:
            x=0
            print("page not exist not found")
            #exit()
            return x
    
"""
fault_link()

Description:

This Python script defines a function `fault_link` that continuously checks for the presence of specific
images on the screen using PyAutoGUI. The images to be located are specified as
"./image/page_not_exist.png", "./image/people_list.png", and "./image/link.png".  The confidence parameter is used for image recognition.

The script clicks on the "people_list" image if found, then attempts to click on the "link" image if it appears.
After clicking on the "link" image, the script calls the `check_fault_link` function to check for the existence of another image.
If the image is found, the script enters a recursive call to the `fault_link` function.

Note: PyAutoGUI and the specified image files are assumed to be available for the script to run successfully.

"""

def fault_link():
    while True:
        x=0
        try:
            x,y=pyautogui.locateCenterOnScreen("./image/page_not_exist.png",confidence=0.8)
        except:
            print("page_not_exist not present ")
        if(x):
            try:
                x,y=pyautogui.locateCenterOnScreen("./image/people_list.png")
            except:
                return
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
                    #time.sleep(2)
                # else:
                #     break
            except:
                print("e")
        else:
            return x



def fault_link_2():
    try:
        x,y=pyautogui.locateCenterOnScreen("./image/people_list.png")
    except:
        return
    pyautogui.click(x,y)
    print("clicked on people_lists")

    try:
        x,y=pyautogui.locateCenterOnScreen("./image/link.png",confidence=0.8)
        pyautogui.moveTo(x,y)
        pyautogui.click(x,y)
        pyautogui.moveTo(1668,308,1)
        pyautogui.click(1668,308)
        print("clicked on link")
    except:
        return
    return