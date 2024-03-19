import pyautogui
import time


"""
check_post()

Description:
This Python function, check_post(), uses PyAutoGUI to locate the center of specific images on the screen, 
representing different options related to posts or activities. The images to be located are 
"./image/show_all_posts.png", "./image/show_all_activity.png", "./image/show_all_comments.png", and "./image/show_all_editions.png". 
The confidence parameter is used for image recognition.

The function attempts to find each image in sequence. If an image is found, it returns the 
x, y coordinates of the center of that image. If none of the images are found, it prints "post/activity/comments not found" 
to the console and returns 0, 0.

Note: PyAutoGUI and the specified image files are assumed to be available for the function to run successfully.

"""

def check_post():
    try:
        while True:
            x,y=pyautogui.locateCenterOnScreen("./image/show_all_posts.png",confidence=0.8)
            return x,y
    except:
        try:
            while True:
                x,y=pyautogui.locateCenterOnScreen("./image/show_all_activity.png",confidence=0.8)
                return x,y
        except:
            try:
                while True:
                    x,y=pyautogui.locateCenterOnScreen("./image/show_all_comments.png",confidence=0.8)
                    return x,y
            except:
                try:
                    while True:
                        x,y=pyautogui.locateCenterOnScreen("./image/show_all_editions.png",confidence=0.8)
                        return x,y
                except:
                    print("post/activity/comments not found")
                    return 0,0


"""
scroll_for_post()

Description:
This Python function, scroll_for_post(), utilizes PyAutoGUI to scroll the screen, specifically scrolling up by 100 units. 
It then calls the check_post() function to identify the presence of certain images on the screen, representing posts or activities. 
The function enters a loop, continually scrolling and checking for posts until no post is found (x coordinate is 0). 
If a post is found, it clicks on the post and prints "clicked on ---" to the console.

Note: PyAutoGUI, the specified image files, and the check_post() function are assumed to be available for the function to run successfully.

"""


def scroll_for_post(): #for the scroll post

    pyautogui.scroll(-100)
    time.sleep(2)
    x,y=check_post()
    #x,y=check_post_tick()
    while True:
        if x==0 :
            scroll_for_post()  
            break
        else:
            pyautogui.click(x,y)
            print("clicked on ---")
            return
            
"""
scroll()

Description:
This Python function, scroll(), utilizes PyAutoGUI to scroll the screen by 300 units. 
It then calls the check_post_tick() function to identify the presence of certain images on the screen,
specifically checking for tick marks associated with posts. The function enters a loop, continually scrolling 
until no tick mark is found (x coordinate is 0).

Note: PyAutoGUI, the specified image files, and the check_post_tick() function are assumed to be available for the function to run successfully.

"""  

def scroll():
    x,y=check_post_tick()
    pyautogui.scroll(-300)
    time.sleep(1)
    # count=0
    # if(count < 2):
    #     pyautogui.scroll(100)
    #     count+=1
    while True:
        if x==0 :
            scroll()
            break
            #x,y=check_post()
        else:
           
            return


"""
check_post_tick()

Description:
This Python function, check_post_tick(), uses PyAutoGUI to locate the center of an image on the screen, 
specifically the "./image/post_tick.png" image. The function is designed to run indefinitely in a while loop, 
attempting to find the image. If the image is found, it returns the x, y coordinates of the center of the located image. 
If the image is not found, an exception is caught, and the function sets x, y coordinates to 0 before returning them.

Note: PyAutoGUI and the specified image file are assumed to be available for the function to run successfully.

"""

def check_post_tick():
    
    while True:
        try:
            x,y=0,0
            x,y=pyautogui.locateCenterOnScreen("./image/post_tick.png")
            return x,y
        except: 
            x,y=0,0
            return x,y

"""
scroll_until_all()

Description:
This Python function, scroll_until_all(), uses PyAutoGUI to perform a series of actions to scroll through 
content on the screen until a specific condition is met. It first moves the mouse to the 
position (905, 469) # which is the center of the screen and enters a loop where it scrolls the screen by 500 
units repeatedly. It checks for the presence of an image representing a post tick using the check_post_tick() function. 
If the image is found, it clicks on another image "./image/back.png" and prints "clicked on back" to the console before returning.
If the image is not found, the function enters a recursive call to itself.

Note: PyAutoGUI and the specified image files are assumed to be available for the function to run successfully.

"""

def scroll_untill_all():
    pyautogui.moveTo(905,469)
    while True:
        pyautogui.scroll(-500)
        try:
            if(check_post_tick()):
                x,y=pyautogui.locateCenterOnScreen("./image/back.png")
                pyautogui.moveTo(x,y)
                pyautogui.click()
                print("clicked on back")
                return
            else:
                scroll_untill_all()
        except:
            print("error")


"""
switch_to_post()

Description:
This Python function, switch_to_post(), uses PyAutoGUI to locate the center of specific images on the screen, 
representing different buttons related to posts. The images to be located are "./image/post.png" and "./image/greenpost.png". 
The function includes a 2-second sleep to allow for screen changes. It attempts to find the "post" button first, and if successful,
it moves the mouse to the button's location and clicks it, printing "Clicked on post button" to the console. 
If the "post" button is not found, it looks for the "greenpost" button and clicks it, printing "Clicked on green post button" 
to the console.

Note: PyAutoGUI and the specified image files are assumed to be available for the function to run successfully.

"""
def switch_to_post():  #Function to switch to the post section on the screen.
    time.sleep(2)
    try:
        x,y=pyautogui.locateCenterOnScreen("./image/post.png",confidence=0.8)
        pyautogui.moveTo(x,y)
        pyautogui.click()
        print("cilcked on post button")
        return
    except:
        x,y=pyautogui.locateCenterOnScreen("./image/greenpost.png",confidence=0.8)
        pyautogui.moveTo(x,y)
        pyautogui.click()
        print("cilcked on green post button")
        return


"""
post_scan()

Description:
This Python function, post_scan(), performs a series of actions to scan through posts on the screen. 
It includes a 2-second sleep and moves the mouse to the position (905, 469) #which is the center of the screen
It then calls the scroll_for_post() function to scroll and check for posts. After a 2-second sleep, 
it calls the switch_to_post() function to switch to the post section. It then calls the scroll() function to continue 
scrolling through posts. If a post is found (checked with check_post_tick()), it clicks on the "./image/back.png" button and 
prints "Clicked on back2" to the console.

Note: PyAutoGUI and the specified image files are assumed to be available for the function to run successfully.

"""
def post_scan():
    time.sleep(2)
    pyautogui.moveTo(905,469)
    scroll_for_post()
    time.sleep(2)
    switch_to_post()

    scroll()
    if(check_post_tick()):
        x,y=pyautogui.locateCenterOnScreen("./image/back.png",confidence=0.8)
        pyautogui.moveTo(x,y)
        pyautogui.click()
        print("clicked on back2")
    return

