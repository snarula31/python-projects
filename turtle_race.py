from random import randint
import turtle as t


is_race_on = False
screen = t.Screen()
screen.setup(width=500, height=400)

colors = ["red", "blue", "orange", "yellow", "green", "purple"]
y_cor = [0, 30, -30, 60, -60, 90]
all_turtles = []
user_bet = screen.textinput(
    title="Make your Bet", prompt=f"Which turtle would place a bet on?(Enter a color) \n {colors}")
user_bet_amt = screen.textinput(
    title="Bet Amount", prompt="Enter amount of money want to bet.")

screen.bgcolor("black")

for t_index in range(0, 6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[t_index])
    new_turtle.goto(x=-235, y=y_cor[t_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 235:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! {winning_color} won the race. ")
            else:
                print(f"You've lost! {winning_color} won the race. ")
        random_dist = randint(0, 15)
        turtle.forward(random_dist)

screen.exitonclick()
