from turtle import Screen, Turtle

screen = Screen()

turtle = Turtle()
turtle.shape('turtle')

deg = 1
step = 1
i = 0
while i < 360:
    turtle.right(deg)
    turtle.forward(step)
    i += 1

screen.mainloop()