import turtle
import pandas

screen = turtle.Screen()

image = "blank_states_img.gif"
screen.addshape(image)

data = pandas.read_csv("50_states.csv")

turtle.shape(image)

correct = 0
answers = []

game = True
while game:
    answer = screen.textinput(title = f"Guess A State {correct}/50", prompt = "Guess A State").title()
    if answer == "Exit":
        break
    is_in = answer in data["state"].values
    if is_in == True and answer not in answers:
        answers.append(answer)
        correct+=1
        data_in = data[data["state"] == answer]
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.setx(int(data_in["x"].item()))
        new_turtle.sety(int(data_in["y"].item()))
        new_turtle.write(answer)

not_guessed = [state for state in data["state"].values if state not in answers]

data_to_csv = {
    "not guessed":not_guessed
}

useable = pandas.DataFrame(data_to_csv)

useable.to_csv("not_guessed_states.csv")