from turtle import Screen
from paddle import Paddle
from pong_ball import Ball
from scoreboard import ScoreBoard
import time

# Screen Set-up
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
# Movement of the paddles
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collion of ball with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # Detects if right paddle missed
    if ball.xcor() > 385:
        ball.reset_pos()
        scoreboard.l_point()

    # Detects if left paddle missed
    if ball.xcor() < -385:
        ball.reset_pos()
        scoreboard.r_point()

    if scoreboard.lscore == 10 or scoreboard.rscore == 10:
        game_is_on = False
        print("Game Over")
screen.exitonclick()
