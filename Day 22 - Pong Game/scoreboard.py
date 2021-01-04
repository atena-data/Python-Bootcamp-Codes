from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.goto((0, 200))
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.l_score} {self.r_score}", align="center", font=("Courier", 60, "normal"))

    def l_score_count(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def r_score_count(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()