from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
colours = ["red", "green", "pink", "maroon", "violet", "blue", "wheat", "gold", "IndianRed", "SeaGreen", "DarkOrchid"]


def draw(num):
    for _ in range(num):
        timmy.fd(100)
        timmy.rt(360/num)

if __name__ == "__main__":
    numFigures = 10
    number = 3
    for _ in range(numFigures):
        timmy.color(random.choice(colours))
        draw(number)
        number += 1

screen = Screen()
screen.exitonclick()

