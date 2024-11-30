from turtle import Screen, Turtle
from plate import Plate
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
game_on = True

l_paddle = Plate((-350, 0))
r_paddle = Plate((350, 0))
l_score = Scoreboard((-350, 280))
r_score = Scoreboard((350, 280))
ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if r_score.score == 3:
        game_on = False
        r_score.winner(player='Right player')

    if l_score.score == 3:
        game_on = False
        l_score.winner(player='Left player')

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect paddle miss on right side
    if ball.xcor() > 380:
        ball.reset_pos()
        l_score.score_update()

    # detect paddle miss on left side
    if ball.xcor() < -380:
        ball.reset_pos()
        r_score.score_update()

screen.exitonclick()
