import turtle as t
import random


t.colormode(255)
t.mode("standard")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour_tuple = (r,g,b)
    return colour_tuple


timmy = t.Turtle()
timmy.shape("turtle")
timmy.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy.pencolor(random_color())
        timmy.circle(100)
        timmy.left(size_of_gap)
    
draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()