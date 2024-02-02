import pyautogui
import time

def check_post_tick():
    try:
        x,y=0,0
        x,y=pyautogui.locateCenterOnScreen("post_tick.png")
        return x,y
    except:
        x,y=0,0
        return x

def scroll_untill_all():
    pyautogui.moveTo(905,469)
    while True:
        pyautogui.scroll(-500)
        if(check_post_tick()):
            x,y=pyautogui.locateCenterOnScreen("back.png")
            return
        else:
            scroll_untill_all()

scroll_untill_all()