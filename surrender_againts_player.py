from main import look_for_img_and_click
import time

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
          3000 / (end_time - start_time))
