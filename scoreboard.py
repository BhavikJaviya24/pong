from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 14, 'normal')


class Scoreboard(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(pos)
        self.score = 0
        self.write(f"Score:{self.score}", False, align=ALIGNMENT, font=FONT)

    def score_update(self):
        self.score += 1
        self.clear()
        self.write(f"Score:{self.score}", False, align=ALIGNMENT, font=FONT)

    def winner(self, player):
        self.goto(0, 50)
        self.write(f"{player} Wins!!", False, align=ALIGNMENT, font=FONT)
