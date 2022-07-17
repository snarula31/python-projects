from turtle import Turtle


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("White")
        self.penup()
        self.goto(0, 0)
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1
        self.move_speed *= 0.9

    def reset_pos(self):
        self.home()
        self.bounce_x()
        self.move_speed = 0.1
