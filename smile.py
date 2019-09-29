from turtle import Screen, Turtle
import math

screen = Screen()

turtle = Turtle()
turtle.shape('turtle')

def draw_shape(shape, radius, dir):
    i = 0
    angle = 10
    length = 2 * math.pi * radius
    step = (length / 360) * angle
    amount = 180 if shape == 'arc' else 360
    while(i < amount):
        turtle.forward(step)
        turtle.right(angle) if dir == 0 else turtle.left(angle)
        i += angle

def smile(radius):
    turtle.begin_fill()
    draw_shape('circle', radius, 1)
    turtle.color('yellow')
    turtle.end_fill()
    turtle.color('black')

    turtle.penup()
    turtle.goto(-(radius * 0.25), (radius * 2) * 0.75)
    turtle.pendown()

    turtle.begin_fill()
    draw_shape('circle', radius * 0.15, 0)
    turtle.color('blue')
    turtle.end_fill()
    turtle.color('black')

    turtle.penup()
    turtle.goto((radius * 0.25) + radius * 0.15, turtle.ycor())
    turtle.pendown()

    turtle.begin_fill()
    draw_shape('circle', radius * 0.15, 0)
    turtle.color('blue')
    turtle.end_fill()
    turtle.color('black')

    turtle.penup()
    turtle.goto(turtle.xcor() - (radius * 0.3), turtle.ycor() - radius * 0.5)
    turtle.pendown()

    turtle.right(90)
    turtle.width(4)
    turtle.forward(radius * 0.25)

    turtle.penup()
    turtle.goto(turtle.xcor() + (radius * 0.25), turtle.ycor() - radius * 0.25)
    turtle.pendown()

    turtle.width(4)
    turtle.color('red')
    draw_shape('arc', radius * 0.25, 0)
    turtle.color('black')

smile(200)

screen.mainloop()