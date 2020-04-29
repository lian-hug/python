#贪吃蛇小游戏#
############################导入数据库###########################
from turtle import *
from random import randrange
from time import sleep
############################定义变量###########################
apple_x = randrange(-19, 19) * 10
apple_y = randrange(-19, 19) * 10
snake=[[0,0],[10,0],[20,0],[30,0],[40,0],[50,0]]
aim_x=10
aim_y=0
############################定义函数###########################
def square(x,y,size,color_name):#定义画小方块（蛇由小方块组成）的函数
    up()
    goto(x,y)
    down()
    color(color_name)
    begin_fill()
    for n in range(4):
        forward(size)
        left(90)
    end_fill()
def inside():#定义小蛇在界面内的函数
    if -200<=snake[-1][0]<=180 and -190<=snake[-1][1]<=190:
        return True
    else:
        return False
def hit_snake():#定义蛇撞到自己的函数
    for n in range(len(snake)-1):
        if snake[-1][0]==snake[n][0] and snake[-1][1]==snake[n][1]:
           return True
    return False
def reset():#定义重新开始的函数
    global apple_x,apple_y,snake,aim_x,aim_y
    sleep(2)
    apple_x = randrange(-19, 19) * 10
    apple_y = randrange(-19, 19) * 10
    snake = [[0, 0], [10, 0], [20, 0], [30, 0], [40, 0], [50, 0]]
    aim_x = 10
    aim_y = 0


def change(x,y):
    global aim_x,aim_y
    aim_x=x
    aim_y=y
def gameLoop():
    global apple_x,apple_y,snake,aim_x,aim_y
    snake.append([snake[-1][0] + aim_x, snake[-1][1] + aim_y])

    for n in range(len(snake)):
        square(snake[n][0], snake[n][1], 10, 'green')

    if snake[-1][0]!=apple_x or snake[-1][1]!=apple_y:
        snake.pop(0)
    else:
        apple_x = randrange(-19, 19) * 10
        apple_y = randrange(-19, 19) * 10
    if not inside() or hit_snake():
        square(snake[-1][0],snake[-1][1],10,'red')
        update()
        reset()
    clear()
    square(-210, -200, 410, 'black')
    square(-200, -190, 390, 'light blue')
    square(apple_x, apple_y, 10, 'yellow')
    for n in range(len(snake)):
        square(snake[n][0], snake[n][1], 10, 'green')
    ontimer(gameLoop,100)
    update()

############################主程序###########################
setup(420,420,0,0)
hideturtle()
tracer(False)
listen()
onkey(lambda :change(0,10),'w')#按键盘上的w，小蛇向上爬
onkey(lambda :change(0,-10),'s')#按键盘上的s，小蛇向下爬
onkey(lambda :change(-10,0),'a')#按键盘上的a，小蛇向左爬
onkey(lambda :change(10,0),'d')#按键盘上的d，小蛇向右爬
gameLoop()
done()
