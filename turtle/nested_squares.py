from turtle import Screen, Turtle

screen = Screen()

turtle = Turtle()
turtle.shape('turtle')

def draw_square(angle, step):
    turtle.forward(step)
    turtle.right(angle)
    turtle.forward(step)
    turtle.right(angle)
    turtle.forward(step)
    turtle.right(angle)
    turtle.forward(step)

def rotate(angle, padding):
    turtle.penup()
    turtle.left(angle)
    turtle.forward(padding)
    turtle.right(angle)
    turtle.forward(padding)
    turtle.right(angle)
    turtle.pendown()

def nested_squares(angle, step, padding, nesting):
    i = 0
    while i < nesting:
        draw_square(90, step)
        rotate(angle, padding)
        step += padding * 2
        i += 1
        
nested_squares(90, 50, 10, 5)

screen.mainloop()