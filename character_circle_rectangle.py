from pico2d import *
import math
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_circle():
    print("circle")
    
    cx , cy , r = 800//2 , 600//2 , 200
    # 그림 그리기
    for deg in range(0,360,1):

        x = cx + r * math.cos(math.radians(deg))
        y = cy + r * math.sin(math.radians(deg))

        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        delay(0.01)

    pass

def run_rectangle():
    print("rectangle")
    pass

while True:
    run_circle()
    run_rectangle()

    break

close_canvas()