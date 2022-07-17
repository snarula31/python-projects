from turtle import Turtle, Screen
import time
import snake
import food
import scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = snake.Snake()
food = food.Food()
scoreboard = scoreboard.ScoreBoard()

# Movements of the snake
screen.listen()
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:  # detects collision with the food
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # detects collision with the wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game_is_on = False
        scoreboard.game_over()

    # detects colliion with the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
# if segment == snake.head:
#   pass
