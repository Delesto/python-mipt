from turtle import Screen, Turtle
import math

screen = Screen()

turtle = Turtle()
turtle.shape('turtle')

i = 0
step = 1
while i < 360:
    turtle.left(6)
    turtle.forward(step)
    step += 0.01
    i += 1

screen.mainloop()