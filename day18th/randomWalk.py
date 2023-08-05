from turtle import Turtle, Screen
import turtle as t
import random

angles = [0, 90, 180, 360]
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour_tuple = (r,g,b)
    return colour_tuple


timmy = Turtle()
timmy.shape("turtle")
timmy.pensize(10)
timmy.speed("fastest")

for _ in range(150):
    timmy.pencolor(random_color())
    timmy.fd(30)
    timmy.setheading(random.choice(angles))

screen = Screen()
screen.exitonclick()
