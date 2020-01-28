import pyautogui
import time


# You need to have open cv to install it type :
# pip install opencv_python
# in Pycharm Terminal

def look_for_img_and_click(img_name, should_wait=False):
    coordinate = pyautogui.locateOnScreen(img_name)
    while coordinate is None:
        coordinate = pyautogui.locateOnScreen(img_name, confidence=.7)
    if should_wait:
        time.sleep(1)
    pyautogui.moveTo(coordinate)
    pyautogui.click()


should_capitulate = True

for i in range(0, 20):
    start_time = time.time()
    if should_capitulate:
        look_for_img_and_click('sprites/1_pret.PNG')
        look_for_img_and_click('sprites/2_param.PNG')
        look_for_img_and_click('sprites/3_capitulation.PNG')
        look_for_img_and_click('sprites/4_ok.PNG')
        look_for_img_and_click('sprites/5_continuer.PNG', should_wait=True)
        should_capitulate = False
    else:
        look_for_img_and_click('sprites/1_pret.PNG')
        look_for_img_and_click('sprites/5_continuer.PNG', should_wait=True)
        should_capitulate = True
    end_time = time.time()
    print('Iteration : ', i, ' Elpased Time : ', end_time - start_time, 's Estimated point per minutes : ',
          6000 / (end_time - start_time))
