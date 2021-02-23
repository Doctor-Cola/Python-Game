from turtle import *

def rectangle(x,y,width,height):
    up()
    goto(x,y)
    begin_fill()
    for i in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()
