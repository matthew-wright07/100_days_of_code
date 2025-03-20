from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.color("blue")
        self.sety(-300)
    def move(self):
        self.sety(self.ycor() + 20)