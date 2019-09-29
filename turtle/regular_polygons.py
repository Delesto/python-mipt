from turtle import Screen, Turtle
import math

screen = Screen()

turtle = Turtle()
turtle.shape('turtle')

def draw_polygon(angle, sides, side_length):
    i = 0
    while i < sides:
        turtle.right(180 - angle / 2 if i < 1 else 180 - angle)
        turtle.forward(side_length)
        i += 1
    turtle.left(angle / 2)

def regular_polygons(n):
    side_length = 50
    growth = 10
    i = 3
    while i < n + 3:
        angle = (i - 2) / i * 180
        radius = side_length / (2 * math.sin(math.radians(360 / (2 * i))))
        next_radius = (side_length + growth) / (2 * math.sin(math.radians(360 / (2 * (i + 1)))))
        draw_polygon(angle, i, side_length)
        
        turtle.penup()
        turtle.forward( next_radius - radius )
        turtle.pendown()

        side_length += growth
        i += 1

regular_polygons(10)

screen.mainloop()