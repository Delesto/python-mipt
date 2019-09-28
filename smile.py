from turtle import Screen, Turtle
import math

screen = Screen()

turtle = Turtle()
turtle.shape('turtle')

def draw_shape(shape, radius, dir):
    i = 0
    angle = 1
    length = 2 * math.pi * radius
    step = (length / 360) * angle
    amount = 180 if shape == 'arc' else 360
    while(i < amount):
        turtle.forward(step)
        turtle.right(angle) if dir == 0 else turtle.left(angle)
        i += angle

def smile(face_radius, eye_radius, nouse_length, smile_radius):
    turtle.begin_fill()
    draw_shape('circle', face_radius, 1)
    turtle.color('yellow')
    turtle.end_fill()
    turtle.color('black')
    
    turtle.penup()
    turtle.goto(-(face_radius * 0.25), (face_radius * 2) * 0.75)
    turtle.pendown()

    turtle.begin_fill()
    draw_shape('circle', eye_radius, 0)
    turtle.color('blue')
    turtle.end_fill()
    turtle.color('black')

    turtle.penup()
    turtle.goto((face_radius * 0.25) + eye_radius, turtle.ycor())
    turtle.pendown()

    turtle.begin_fill()
    draw_shape('circle', eye_radius, 0)
    turtle.color('blue')
    turtle.end_fill()
    turtle.color('black')

    turtle.penup()
    turtle.goto(turtle.xcor() - eye_radius * 2, turtle.ycor() - (eye_radius) - face_radius * 0.25)
    turtle.pendown()

    turtle.right(90)
    turtle.width(10)
    turtle.forward(nouse_length)

    turtle.penup()
    turtle.goto(turtle.xcor() + eye_radius * 2, turtle.ycor() - face_radius * 0.25)
    turtle.pendown()

    turtle.width(8)
    turtle.color('red')
    draw_shape('arc', smile_radius, 0)
    turtle.color('black')

smile(100, 15, 30, 30)

screen.mainloop()