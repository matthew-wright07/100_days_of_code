from turtle import Screen, Turtle
import time
screen = Screen()

class Snake:
    def __init__(self):
        self.position = 0
        self.segments = []
        for i in range(0,3):
            new_turtle = Turtle("square")
            new_turtle.penup()
            new_turtle.setx(self.position)
            self.position-=20
            new_turtle.color("white")
            self.segments.append(new_turtle)
            
    def move(self):
        for i in range(len(self.segments)-1,0,-1):
                self.segments[i].goto(self.segments[i-1].xcor(),self.segments[i-1].ycor())
        self.segments[0].forward(20)
        screen.update()
        time.sleep(0.1)
    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
    def extend(self):
        new_turtle = Turtle("square")
        new_turtle.penup()
        new_turtle.goto(self.segments[-1].position())
        new_turtle.color("white")
        self.segments.append(new_turtle)
