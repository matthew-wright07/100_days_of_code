import game_data
import random

data = game_data.data
score = 0

random_choice1 = random.choice(data)

while True:
    random_choice2 = random.choice(data)
    print(f"Compare A: {random_choice1['name']} a {random_choice1['description']} from {random_choice1['country']}")
    print("\nor\n")
    print(f"Compare B: {random_choice2['name']} a {random_choice2['description']} from {random_choice2['country']}")
    answer = input("Who has more followers? Type 'A' or 'B'\n").lower()
    if answer == "a" and random_choice1["follower_count"]>random_choice2["follower_count"]:
        print("You're right!")
        score+=1
        print(f"Your score is : {score}")
        random_choice1=random_choice1
    elif answer == "b" and random_choice1["follower_count"]<random_choice2["follower_count"]:
        print("You're right!")
        score+=1
        print(f"Your score is : {score}")
        random_choice1=random_choice2
    else:
        print("You lose! Game over.")
        print(f"Your final score was {score}")
        break