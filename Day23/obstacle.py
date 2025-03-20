from turtle import Turtle
import random

class Obstacle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.setx(random.randint(100,300))
        self.sety(random.randint(-300,300))
        self.object_speed = random.randint(1,10)
    def move(self):
        if self.xcor()<-300:
            self.setx(random.randint(100,300))
        self.setx(self.xcor() - self.object_speed)
    def level_up(self):
        self.object_speed+=1
    