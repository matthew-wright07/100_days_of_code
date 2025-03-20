from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.pencolor("white")
        self.pendown()
        self.hideturtle()
        self.write(f"Score: {self.score}",align="center",font=("Arial", 20, "bold"))
    def plus(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}",align="center",font=("Arial", 20, "bold"))
    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write("GAME OVER",align="center",font=("Arial", 20, "bold"))