from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.sety(280)
        self.pendown()
        self.score = 0
        self.write(f"Score: {self.score}",align="center", font=("Arial", 16, "normal"))
        self.hideturtle() 
    def add(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}",align="center", font=("Arial", 16, "normal"))
    def game_over(self):
        self.penup()
        self.sety(0)
        self.pendown()
        self.write("Game Over",align="center", font=("Arial", 20, "bold"))
