import turtle as t
import random

t.colormode(255)
t.mode("standard")

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

timmy = t.Turtle()
timmy.speed("fastest")
timmy.ht()

pos_y = -225
for _ in range(10):
    timmy.penup()
    timmy.setpos(-225, pos_y)
    timmy.pendown()
    for _ in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.penup()
        timmy.fd(50)
        timmy.pendown()
    pos_y += 50



screen = t.Screen()
screen.exitonclick()

"""
colors = colorgram.extract('image.jpg', 30)
rgb_colors = []

for color in colors:
    red = color.rgb.r
    green = color.rgb.g
    blue = color.rgb.b
    rgb_tuple = (red, green, blue)
    rgb_colors.append(rgb_tuple)

print(rgb_colors)
"""