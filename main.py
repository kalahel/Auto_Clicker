import pyautogui
import time


# You need to have open cv to install it type :
# pip install opencv_python
# in Pycharm Terminal

def look_for_img_and_click(img_name, should_wait=False):
    print('looking for : ', img_name)
    coordinate = pyautogui.locateOnScreen(img_name, confidence=.85)
    while coordinate is None:
        coordinate = pyautogui.locateOnScreen(img_name, confidence=.65)
    if should_wait:
        time.sleep(2)
    pyautogui.moveTo(coordinate)
    pyautogui.click()
    print('clicked on : ', img_name)

