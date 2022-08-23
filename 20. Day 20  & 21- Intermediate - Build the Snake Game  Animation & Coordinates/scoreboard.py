from turtle import Turtle

ALIGHNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0

        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.update_Scoreboard()

    def update_Scoreboard(self):
        self.write(f"Score {self.score}", align=ALIGHNMENT, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"Game Over !!!", align=ALIGHNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_Scoreboard()
