import pyautogui


# You need to have open cv to install it type :
# pip install opencv_python
# in Pycharm Terminal

def look_for_img_and_click(img_name):
    coordinate = pyautogui.locateOnScreen(img_name)
    while coordinate is None:
        coordinate = pyautogui.locateOnScreen(img_name, confidence=.7)
    pyautogui.moveTo(coordinate)
    pyautogui.click()


should_capitulate = True

for i in range(0, 3):
    if should_capitulate:
        look_for_img_and_click('sprites/1_pret.PNG')
        look_for_img_and_click('sprites/2_param.PNG')
        look_for_img_and_click('sprites/3_capitulation.PNG')
        look_for_img_and_click('sprites/4_ok.PNG')
        look_for_img_and_click('sprites/5_continuer.PNG')
        should_capitulate = False
    else :
        look_for_img_and_click('sprites/1_pret.PNG')
        look_for_img_and_click('sprites/5_continuer.PNG')
        should_capitulate = True
