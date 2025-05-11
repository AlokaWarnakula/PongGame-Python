from turtle import Turtle

ALIGN = 'center'
FONT = ('Comic Sans MS', 20, 'bold')
LOSE = ('Comic Sans MS', 40, 'bold')


class ScoreBoard(Turtle):

    def __init__(self, position, sidePlayer):
        super().__init__()
        self.score = 0
        self.sidePlayer = sidePlayer
        self.color("plum")
        self.penup()
        self.hideturtle()
        self.goto(position)  # title location
        self.writingScore()

    def addScore(self):
        self.score += 1
        self.clear()
        self.writingScore()

    def writingScore(self):
        score = self.score
        side = self.sidePlayer
        self.write(f"Total Score {side} is: {score}", move=False, align=ALIGN, font=FONT)

    def missBall(self):
        side = self.sidePlayer
        self.goto(0, 0)
        self.write(f"{side} player missed the ball and lost", move=False, align=ALIGN, font=LOSE)
