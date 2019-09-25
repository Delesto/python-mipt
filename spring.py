from turtle import Screen, Turtle
import math

screen = Screen()

turtle = Turtle()
turtle.shape('turtle')
turtle.speed(10)

def draw_arc(radius):
    i = 0
    angle = 1
    length = 2 * math.pi * radius
    step = (length / 360) * angle
    while(i < 180):
        turtle.forward(step)
        turtle.right(angle)
        i += angle

def spring(length):
    turtle.left(90)
    i = 0
    radius_l = 10
    radius_h = 50
    while(i < length):
        draw_arc(radius_h)
        if(i == length - 1):
            break
        draw_arc(radius_l)
        i += 1

spring(4)

screen.mainloop()