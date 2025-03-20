from turtle import Turtle,Screen
from ball import Ball
from paddle import Paddle
from score import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.tracer(0)

ball = Ball()
paddle1 = Paddle(-250)
paddle2 = Paddle(250)
score = Score()

screen.listen()
screen.onkey(paddle1.moveup,"w")
screen.onkey(paddle1.movedown,"s")
screen.onkey(paddle2.moveup,"Up")
screen.onkey(paddle2.movedown,"Down")

should_continue = True

while should_continue:
    if ball.distance(paddle1) < 50 and ball.xcor()<-235:
        ball.switchx()
    if ball.distance(paddle2) < 50 and ball.xcor()>235:
        ball.switchx()
    if ball.xcor() > 300:
        score.left_score()
        ball.reset()
    if ball.xcor() < -300:
        score.right_score()
        ball.reset()
    
    time.sleep(0.02)
    ball.move()
    screen.update()

screen.exitonclick()
