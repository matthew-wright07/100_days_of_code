from turtle import Screen
from player import Player
from obstacle import Obstacle
from score import Score
import time

screen = Screen()
screen.tracer(0)

player = Player()
score = Score()

obstacles = []
for _ in range(0,25):
    obstacle = Obstacle()
    obstacles.append(obstacle)

screen.listen()
screen.onkey(player.move,"Up")

should_continue = True

while should_continue:
    for item in obstacles:
        item.move()
        if player.distance(item)<20:
            should_continue = False
            score.game_over()
    if player.ycor()>250:
        score.add()
        player.sety(-300)
        for item in obstacles:
            item.level_up()
    time.sleep(.1)
    screen.update()

screen.exitonclick()