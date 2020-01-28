import pyautogui
import time
import fileinput


def look_for_img_and_click(img_name, should_wait=False):
    coordinate = pyautogui.locateOnScreen(img_name)
    while coordinate is None:
        coordinate = pyautogui.locateOnScreen(img_name, confidence=.7)
    if should_wait:
        time.sleep(2)
    pyautogui.moveTo(coordinate)
    pyautogui.click()


should_capitulate = True

print("Should surrender first ? y/n")
for line in fileinput.input():
    pass
    line.rstrip()
    line = ''.join(filter(str.isalpha, line))
    if line == 'y':
        should_capitulate = True
        print("This player will surrender first")
        break
    if line == "n":
        should_capitulate = False
        print("This player will not surrender first")
        break

while True:
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
    print(' Elpased Time : ', end_time - start_time, 's Estimated point per minutes : ',
          3000 / (end_time - start_time))
