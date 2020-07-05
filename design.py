import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor('black')
Mohit = turtle.Turtle()
Mohit.speed(0)
Mohit.color('white')
rotate = int(360)


def drawCircles(t, size):
    for i in range(10):
        t.circle(size)
        size = size - 4


def drawSpecial(t, size, repeat):
    for i in range(repeat):
        drawCircles(t, size)
        t.right(360 / repeat)


drawSpecial(Mohit, 100, 10)
Bhavesh = turtle.Turtle
Bhavesh.speed(0)
Bhavesh.color('yellow')
rotate = int(90)


def drawCircles(t, size):
    for i in range(4):
        t.circle(size)
        size = size - 10


def drawSpecial(t, size, repeat):
    for i in range(repeat):
        drawCircles(t, size)
        t.right(360 / repeat)


drawSpecial(Bhavesh, 100, 10)
Mayur = turtle.Turtle()
Mayur.speed(0)
Mayur.color('blue')
rotate = int(80)


def drawCirlcles(t, size):
    for i in range(4):
        t.circle(size)
        size = size - 5


def drawSpecial(t, size, repeat):
    for i in range(repeat):
        drawCircles(t, size)
        t.right(360 / repeat)


drawSpecial(Mayur, 100, 10)
Kapil = turtle.Turtle()
Kapil.speed(0)
Kapil.color('orange')
rotate = int(90)


def drawCirlcles(t, size):
    for i in range(4):
        t.circle(size)
        size = size - 19


def drawSpecial(t, size, repeat):
    for i in range(repeat):
        drawCircles(t, size)
        t.right(360 / repeat)


drawSpecial(Kapil, 100, 10)
Rohit = turtle.Turtle()
Rohit.speed(0)
Rohit.color('pink')
rotate = int(90)


def drawSpecial(t, size, repeat):
    for i in range(repeat):
        drawCircles(t, size)
        t.right(360 / repeat)


drawSpecial(Rohit, 100, 10)

turtle.getscreen()._root.mainloop()
