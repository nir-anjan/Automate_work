import pyautogui
import time

def check_post():#checks for show all stuff
    try:
        while True:
            x,y=pyautogui.locateCenterOnScreen("show_all_posts.png")
            return x,y
    except:
        try:
            while True:
                x,y=pyautogui.locateCenterOnScreen("show_all_activity.png")
                return x,y
        except:
            try:
                while True:
                    x,y=pyautogui.locateCenterOnScreen("show_all_comments.png")
                    return x,y
            except:
                try:
                    while True:
                        x,y=pyautogui.locateCenterOnScreen("show_all_editions.png")
                        return x,y
                except:
                    print("post/activity/comments not found")
                    return 0,0




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
            print("clicked on ----")
            return
            
    

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
            


def check_post_tick():
    
    while True:
        try:
            x,y=0,0
            x,y=pyautogui.locateCenterOnScreen("post_tick.png")
            return x,y
        except: 
            x,y=0,0
            return x,y

def scroll_untill_all():
    pyautogui.moveTo(905,469)
    while True:
        pyautogui.scroll(-500)
        try:
            if(check_post_tick()):
                x,y=pyautogui.locateCenterOnScreen("back.png")
                pyautogui.moveTo(x,y)
                pyautogui.click()
                print("clicked on back")
                return
            else:
                scroll_untill_all()
        except:
            print("error")

def switch_to_post():
    time.sleep(2)
    try:
        x,y=pyautogui.locateCenterOnScreen("post.png")
        pyautogui.moveTo(x,y)
        pyautogui.click()
        print("cilcked on post button")
        return
    except:
        x,y=pyautogui.locateCenterOnScreen("greenpost.png")
        pyautogui.moveTo(x,y)
        pyautogui.click()
        print("cilcked on green post button")
        return

def post_scan():
    time.sleep(2)
    pyautogui.moveTo(905,469)
    scroll_for_post()
    time.sleep(2)
    switch_to_post()

    scroll()
    if(check_post_tick()):
        x,y=pyautogui.locateCenterOnScreen("back.png")
        pyautogui.moveTo(x,y)
        pyautogui.click()
        print("clicked on back2")
    return

