from turtle import Screen, Turtle

screen = Screen()

turtle = Turtle()
turtle.shape('turtle')
turtle.speed(10)

def star(n, length):
    i = 0
    while(i < n):
        turtle.forward(length)
        turtle.right(180 - (180 / n))
        i += 1

star(5, 400)

screen.mainloop()