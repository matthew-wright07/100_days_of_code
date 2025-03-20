import random

randomInt = random.randint(0,2)

userInput = input("Please type 0 for rock, 1 for paper, or 2 for scissors\n")

if userInput == "0" and randomInt == 0:
    print("Computer choose rock. It is a tie!")
elif userInput == "0" and randomInt == 1:
    print("Computer choose paper. You lose!")
elif userInput == "0" and randomInt == 2:
    print("Computer choose scissors. You win!")
elif userInput == "1" and randomInt == 0:
    print("Computer choose rock. You win!")
elif userInput == "1" and randomInt == 1:
    print("Computer choose papper. You tie!")
elif userInput == "1" and randomInt == 2:
    print("Computer choose scissors. You lose!")
elif userInput == "2" and randomInt == 0:
    print("Computer choose rock. You lose!")
elif userInput == "2" and randomInt == 1:
    print("Computer choose papper. You win!")
elif userInput == "2" and randomInt == 2:
    print("Computer choose scissors. You tie!")