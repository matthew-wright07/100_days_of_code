from turtle import Turtle, Screen
import turtle as t
import random
import colorgram
colors = colorgram.extract('hurst.jpg', 30)
new_colors = []
for color in colors:
    new_colors.append((color.rgb.r,color.rgb.g,color.rgb.b))

print(new_colors)
tim = Turtle()

tim.speed('fastest')
t.colormode(255)
tim.width(2.5)
tim.penup()
tim.setx(-400)
tim.sety(-300)

for i in range(0,10):
    for i in range(0,10):
        tim.dot(20, random.choice(new_colors))
        tim.setx(tim.xcor()+50)
    tim.sety(tim.ycor() + 50)
    tim.setx(-400)

screen = Screen()
screen.exitonclick()