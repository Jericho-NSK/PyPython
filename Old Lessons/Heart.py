from time import sleep
from turtle import *

hideturtle()


def move(a, col):
    penup()
    goto(2 * a, a)
    left(90)
    speed(2)
    color(col)
    pendown()
    pensize(5)
    circle(a, 180)
    speed(0)
    right(180)
    speed(1)
    circle(a, 180)
    goto(0, -a)
    goto(2 * a, a)
    speed(0)
    goto(0, 0)


def col(a, col):
    speed(10)
    color(col)
    begin_fill()
    move(a, col)
    end_fill()


col(150, 'red')
sleep(3)
