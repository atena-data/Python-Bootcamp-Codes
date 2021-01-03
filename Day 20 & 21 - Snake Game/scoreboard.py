from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.write(arg=f"Score: {self.score}", align="center", font=("arial", 20, "normal"))
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.color("white")
        self.write(arg="Game Over", align="center", font=("arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", align="center", font=("arial", 20, "normal"))
