from turtle import Screen, Turtle

screen = Screen()

turtle = Turtle()
turtle.shape('turtle')
turtle.speed(10)

def draw_circle(dir):
    i = 0
    step = 10
    angle = 10
    while(i < 36):
        turtle.forward(step)    
        turtle.right(angle) if dir == 0 else turtle.left(angle)
        i += 1

def flower(n):
    i = 0
    while(i < n):
        if(bool((i + 1) % 3 == 0)):
            turtle.right(60)
            n += 1
        else:
            draw_circle(i % 2)
        i += 1

flower(6)

screen.mainloop()