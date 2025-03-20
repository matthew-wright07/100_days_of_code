from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win? Enter a color").lower()
colors = ["red","orange","yellow","green","blue"]
turtles = []
y_postition = -100

for item in colors:
    turtle = Turtle("turtle")
    turtle.penup()
    turtle.color(item)
    turtle.goto(x=-230, y = y_postition)
    turtles.append(turtle)
    y_postition+=50

should_continue = True

while should_continue:
    for i in range(0,len(turtles)):
        if turtles[i].xcor() >= 200:
            should_continue = False
            print(f"Turtle {colors[i]} has won.")
            if user_bet == colors[i]:
                print("Yay you have guessed correctly")
            else:
                print(f"You guessed {user_bet}. Better luck next time")
        random_int = random.randint(0,10)
        turtles[i].forward(random_int)

screen.exitonclick()