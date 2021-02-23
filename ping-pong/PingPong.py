##导入轮子
from random import  random,choice
from turtle import  *
from random import  *
from time import sleep
from gamebase import  rectangle

player=[0,-140]
ball=[0,140]
direction=[choice([-2,-1,1,2]),choice([-2,-1])]

def move(aim):
    player[0] += aim

#判断是否死亡
def bounce():
    if ball[0]<=-300 or ball[0]>=290:
        direction[0]=-direction[0]

    elif ball[1]>=150:
        direction[1]=-direction[1]

    elif ball[1]<=-140+15 and player[0]<=ball[0]<=player[0]+70:
        direction[1]=-direction[1]

def outside():
    if ball[1]<=-140 :return True

##画球
def draw():
    clear()
    up()
    goto(ball[0],ball[1])
    dot(10,'red')
    rectangle(player[0],player[1],70,10)
    update()

##游戏主循环
def gameLoop():
    global ball,direction
    
    bounce()
    ball[0] += direction[0]*2
    ball[1] += direction[1]*2
    draw()

    if outside():
        sleep(2)
        
        #充值游戏数据
        player=[0,-140]
        ball=[0,140]
        direction=[choice([-2,-1,1,2]),choice([-2,-1])]
    ontimer(gameLoop,50)

setup(620,320,0,0)
hideturtle()
tracer(False)
listen()
onkey(lambda:move(20),'d')
onkey(lambda:move(-20),'a')
gameLoop()
done()
