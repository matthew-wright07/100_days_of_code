import random

word_list = ["arrdvark","baboon","camel"]
random_word = random.choice(word_list)

guesses = []
lives = 6
game_over = False

while not game_over:
    print("_"*len(random_word))
    user_letter = input("Guess a letter\n").lower()

    guesses.append(user_letter)

    if user_letter not in random_word:
            lives -= 1

    response = ""

    for letter in random_word:
        if letter in guesses:
            response+=letter
        else:
            response+="_"
    if "_" not in response:
        game_over=True
    if lives==0:
        game_over=True

    print(response)
    print("You have "+str(lives)+" lives left")
print("Game Over")