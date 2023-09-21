from pico2d import *
import math
open_canvas()
#에자일 방법론
grass = load_image('grass.png')
character = load_image('character.png')

def render_frame(x,y):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    delay(0.01)

def run_circle():
    print("circle")
    
    cx , cy , r = 800//2 , 600//2 , 200
    # 그림 그리기
    for deg in range(0,360,1):

        x = cx + r * math.cos(math.radians(deg))
        y = cy + r * math.sin(math.radians(deg))

        render_frame(x,y)

def run_rectangle():
    print("rectangle")

#    for x in range(50,750+1,10):
#        render_frame(x,90)

    for y in range(90,561,10):
        render_frame(750,y)

#    for x in range(750,50-1,-10):
#        render_frame(x,550)


while True:
    run_rectangle()
    #run_circle()
    break

close_canvas()