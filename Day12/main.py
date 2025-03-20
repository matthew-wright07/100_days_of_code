import random

random_number = random.randint(1,100)
lives = 0
guessing = True

def check(num):
    num = int(num)
    if num<random_number:
        return "Too small"
    elif num>random_number:
        return "Too big"
    else:
        return "You win"


print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard'\n")

if difficulty=="easy":
    lives = 10
elif difficulty=="hard":
    lives=5
else:
    print("Wrong input")
print(f"You have {lives} lives left")

while guessing:
    number = input("Make a guess\n")
    response = check(number)
    print(response)
    if response == "You win":
        break
    else:
        lives -=1
        if lives == 0:
            print("Game over.")
            break
        print("Guess Again")
        print(f"You have {lives} lives left")



