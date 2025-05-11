from turtle import Turtle
import random

COLORS = [
    "red", "lime", "yellow", "cyan", "magenta", "orange",
    "deep pink", "turquoise", "gold", "chartreuse", "aqua",
    "blue", "violet", "purple", "spring green", "tomato",
    "dodger blue", "salmon", "medium slate blue", "green yellow"
]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.Xmove = 10
        self.Ymove = 10
        self.ball_speed = 0.1

    def move(self):
        x = self.xcor() + self.Xmove
        y = self.ycor() + self.Ymove
        self.goto(x, y)

    def bounceY(self):
        self.Ymove *= -1
        self.color(random.choice(COLORS))

    def bounceX(self):
        self.Xmove *= -1
        self.ball_speed *= 0.9
        self.color(random.choice(COLORS))

    def resetPosition(self):
        self.goto(0, 0)
        self.bounceX()
