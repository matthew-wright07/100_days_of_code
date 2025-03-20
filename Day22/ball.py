from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.sety(random.randint(-300,300))
        self.x_move = 5
        self.y_move = 2.5
        self.shape("circle")
        self.color("white")
    def move(self):
        if self.ycor()>300 or self.ycor()<-300:
            self.switchy()
        if self.xcor()>300 or self.xcor()<-300:
            self.switchx()

        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)
    def switchx(self):
        self.x_move*= -1
    def switchy(self):
        self.y_move*= -1
    def reset(self):
        self.sety(random.randint(-300,300))
        self.setx(0)




