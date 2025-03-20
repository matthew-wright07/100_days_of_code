from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")
        self.setx(x)
        self.y = 0
    def moveup(self):
        self.y+=20
        self.sety(self.y)
    def movedown(self):
        self.y-=20
        self.sety(self.y)




