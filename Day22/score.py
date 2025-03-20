from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.sety(270)
        self.scores = [0,0]
        self.write(f"{self.scores[0]}     {self.scores[1]}",align="center", font=("Arial", 24, "bold"))
    def left_score(self):
        self.clear()
        self.scores[0] += 1
        self.write(f"{self.scores[0]}     {self.scores[1]}",align="center", font=("Arial", 24, "bold"))
    def right_score(self):
        self.clear()
        self.scores[1] += 1
        self.write(f"{self.scores[0]}     {self.scores[1]}",align="center", font=("Arial", 24, "bold"))

