from turtle import Turtle, Screen
from paddles import Padel
from ball import Ball
from scoreboard import ScoreBoard
import time

# classes init
aloka = Turtle()
screen = Screen()

# screen set up
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(height=500, width=1000)

# scree half line
aloka.pencolor("white")
aloka.penup()
aloka.setheading(270)
aloka.pensize(5)
aloka.goto(x=0, y=250)
aloka.hideturtle()

for i in range(25):
    aloka.pendown()
    aloka.forward(10)
    aloka.penup()
    aloka.forward(10)

# padel init
padelRight = Padel((480, 0))
padelLeft = Padel((-480, 0))

# ball init
ball = Ball()

# scoreboard
scoreboardRight = ScoreBoard((250,220),"Right")
scoreboardLeft = ScoreBoard((-250,220),"Left")

# key define
screen.listen()
screen.onkey(fun=padelRight.up, key="Up")
screen.onkey(fun=padelRight.down, key="Down")
screen.onkey(fun=padelLeft.up, key="w")
screen.onkey(fun=padelLeft.down, key="s")

gameOn = True

while gameOn:
    time.sleep(ball.ball_speed)
    ball.move()

    # wall top and bottom bounce
    if ball.ycor() > 230 or ball.ycor() < -230:
        ball.bounceY()

    # Right paddle collision
    if ball.xcor() > 450 and ball.distance(padelRight) < 50:
        ball.bounceX()
        scoreboardRight.addScore()
        scoreboardRight.writingScore()

    # Left paddle collision
    if ball.xcor() < -450 and ball.distance(padelLeft) < 50:
        ball.bounceX()
        scoreboardLeft.addScore()
        scoreboardLeft.writingScore()

    # check ball missed the right paddle
    if ball.xcor() > 470:
        scoreboardRight.missBall()
        break
    # check ball missed the left paddle
    if ball.xcor() < -470:
        scoreboardLeft.missBall()
        break


screen.exitonclick()
