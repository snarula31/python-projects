from turtle import Turtle

FONT = ("Courier", 20, "normal")
FONT1 = ("Courier", 48, "bold")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("silver")
        self.display_lvl()

    def display_lvl(self):
        self.goto(-285, 260)
        self.write(f"Level: {self.level}", align="Left", font=FONT)

    def increase_lvl(self):
        self.level += 1
        self.clear()
        self.display_lvl()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT1)
