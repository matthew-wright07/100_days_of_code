import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]


while True:
    should_play = input("Do you want to play a game of blackjack? Type 'yes' to play or 'no' to not play\n")
    if should_play == "no":
        break
    computer_cards = []
    user_cards = []

    while sum(computer_cards)<17:
        if 11 in computer_cards and sum(computer_cards)>21:
                for number in range(len(computer_cards)):
                    if computer_cards[number] == 11 and sum(computer_cards) > 21:
                        computer_cards[number] = 1
                        break
        computer_cards.append(random.choice(cards))

    user_cards.append(random.choice(cards))
    user_cards.append(random.choice(cards))

    print(f"Your cards: {user_cards}")
    print(f"Computer's first card: [{computer_cards[0]}]")

    while True:
        another = input("Type 'yes' to get another card or type 'no' to pass\n")

        if another.lower()=="yes":
            user_cards.append(random.choice(cards))
            if 11 in user_cards and sum(user_cards)>21:
                for number in range(len(user_cards)):
                    if user_cards[number] == 11 and sum(user_cards) > 21:
                        user_cards[number] = 1
                        break
            print(user_cards)
        else:
            print(f"Your cards: {user_cards}")
            print(f"Computers cards: {computer_cards}")
            if sum(computer_cards)>21 and sum(user_cards) > 21:
                print("It's a tie!")
            if sum(user_cards) > 21:
                print("You bust! You lose.")
            elif sum(computer_cards) > 21:
                print("Computer busts! You win.")
            elif sum(user_cards) > sum(computer_cards):
                print("You win!")
            elif sum(user_cards) < sum(computer_cards):
                print("You lose.")
            else:
                print("It's a tie!")
            break
