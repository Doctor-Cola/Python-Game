##导入轮子
from turtle import *
from gamebase import square
from random import randrange
from time import sleep

snake=[[0,0],[10,0],[20,0],[30,0],[40,0],[50,0]]

apple_x=randrange(-200,180,10)
apple_y=randrange(-190,190,10)

aim_x=10
aim_y=0

def inside():
    if -200<=snake[-1][0]<=180 and -190<=snake[-1][1]<=190:
        return True 
    else :
        return False

def change(x,y):
    global aim_x,aim_y
    aim_x=x 
    aim_y=y 

#控制蛇移动
def move():
    listen()
    onkey(lambda: change(0,10),'Up')
    onkey(lambda: change(-10,0),'Left')
    onkey(lambda: change(0,-10),'Down')
    onkey(lambda: change(10,0),'Right')
    onkey(lambda: change(0,10),'w')
    onkey(lambda: change(-10,0),'a')
    onkey(lambda: change(0,-10),'s')
    onkey(lambda: change(10,0),'d')
    onkey(lambda: change(0,10),'W')
    onkey(lambda: change(-10,0),'A')
    onkey(lambda: change(0,-10),'S')
    onkey(lambda: change(10,0),'D')

def gameLoop():
    global apple_x,apple_y,aim_x,aim_y,snake

    #画蛇
    snake.append([ snake[-1][0]+aim_x , snake[-1][1]+aim_y ])
    
    

    if snake[-1][0]!=apple_x or snake[-1][1]!=apple_y:
        snake.pop(0)
    else :
        apple_x=randrange(-200,180,10)
        apple_y=randrange(-190,190,10)
    
    if not inside():
        square(snake[-1][0],snake[-1][1],10,'red')
        update()
        sleep(2)
        
        #重置游戏数据
        snake=[[0,0],[10,0],[20,0],[30,0],[40,0],[50,0]]

        apple_x=randrange(-200,180,10)
        apple_y=randrange(-190,190,10)

        aim_x=10
        aim_y=0

    clear()
    
    #画场景
    square(-210,-200,410,'black')
    square(-200,-190,390,'white')
    square(apple_x,apple_y,10,'red')
    
    #让蛇动起来
    for n in range(len(snake)):
        square(snake[n][0],snake[n][1],10,'black')
    ontimer(gameLoop,300)
    
    update()

##画苹果
setup(420,420,0,0)
hideturtle()
tracer(False)
gameLoop()

#控制蛇移动
move()

done()
