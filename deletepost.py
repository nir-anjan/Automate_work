import pyautogui
from time import sleep

sleep(2)
while True:
    try:
        while True :

            sleep(1)

            x,y=pyautogui.locateCenterOnScreen("./NEW_IMAGES/DOTS.png",confidence=0.8)
            pyautogui.moveTo(x,y)
            pyautogui.click(x,y)

            sleep(1)

            x,y=pyautogui.locateCenterOnScreen("./NEW_IMAGES/DEL.png",confidence=0.8)
            pyautogui.moveTo(x,y)
            pyautogui.click(x,y)

            sleep(1)

            x,y=pyautogui.locateCenterOnScreen("./NEW_IMAGES/delete.png",confidence=0.8)
            pyautogui.moveTo(x,y)
            pyautogui.click(x,y)

            sleep(1)

            pyautogui.scroll(-100)

            sleep(1)

    except:
        pyautogui.scroll(-100)
