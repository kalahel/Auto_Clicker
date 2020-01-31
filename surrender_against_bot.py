import time

from main import look_for_img_and_click

# You stop winning points after 10 games
for i in range(0, 10):
    start_time = time.time()
    look_for_img_and_click('sprites/6_jouer.PNG')
    look_for_img_and_click('sprites/2_param.PNG')
    look_for_img_and_click('sprites/3_capitulation.PNG')
    look_for_img_and_click('sprites/4_ok.PNG')
    look_for_img_and_click('sprites/5_continuer.PNG', should_wait=True)
    end_time = time.time()
    print('Iteration : ', i, ' Elpased Time : ', end_time - start_time, 's')
