from turtle import Screen, Turtle
import math

screen = Screen()

turtle = Turtle()
turtle.shape('turtle')
turtle.speed(10)

def draw_circle(radius, dir):
    i = 0
    angle = 10
    length = 2 * math.pi * radius 
    step = (length / 360) * angle
    while(i < 360):
        turtle.forward(step)    
        turtle.right(angle) if dir == 0 else turtle.left(angle)
        i += angle

def butterfly(n):
    radius = 50
    i = 0
    turtle.right(90)
    while(i < n):
        if((i + 1) % 3 == 0):
            radius += 10
            n += 1
        else:
            draw_circle(radius, i % 2)
        i += 1

butterfly(20)

screen.mainloop()