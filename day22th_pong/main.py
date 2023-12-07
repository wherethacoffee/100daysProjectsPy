from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "i")
screen.onkey(r_paddle.go_down, "k")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()
    # Detect collisions with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #Detect collisions with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() < 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.r_point()
    
    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.l_point()

screen.exitonclick()
