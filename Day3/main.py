print("Welcome To Sigma's Lair You Need To Find The Alpha\n")
choice1 = input("You see two doors, one on the left and one on the right. Which door do you choose? (left/right)\n").lower()
if choice1 == "left":
    choice2 = input("There is a bird do you attack or sneak past it\n").lower()
    if choice2 == "sneak":
        choice3 = input("You find a river, do you swim across, go around, or jump over it (across/around/jump)\n").lower()
        if choice3 == "jump":
            print("You found the alpha, you win\n")
        else:
            print("You got eaten by a capybara, you died\n")
    else:
        print("The bird attacked you, you died\n")
else:
    print("You died, you are not the sigma\n")