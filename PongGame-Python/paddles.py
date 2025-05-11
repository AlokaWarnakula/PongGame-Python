from turtle import Turtle


class Padel(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    # up function
    def up(self):
        if self.ycor() < 200:
            y = self.ycor()
            self.sety(y + 40)

    # down function
    def down(self):
        if self.ycor() > -200:
            y = self.ycor()
            self.sety(y - 40)
