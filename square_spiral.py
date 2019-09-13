from turtle import Screen, Turtle

screen = Screen()

turtle = Turtle()
turtle.shape('turtle')

def square_spiral(n):
    i = 0
    step = 10
    while i < n * 4:
        if(i % 2 == 0):
            step += 10
        turtle.forward(step)
        turtle.right(90)
        i += 1 

square_spiral(10)

screen.mainloop()