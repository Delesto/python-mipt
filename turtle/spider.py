from turtle import Screen, Turtle

screen = Screen()

turtle = Turtle()
turtle.shape('turtle')

def spider(length, n):
    angle = 360 / n
    i = 0
    while(i < n):
        turtle.forward(length)
        turtle.stamp()
        turtle.right(180)
        turtle.forward(length)
        turtle.right(180 + angle)
        i += 1

spider(100, 8)

screen.mainloop()