from menu import resources, money

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = money["value"]

def check_resources(type):
    if type == "espresso" and water>=50 and coffee>=18:
        print("There is enough resources")
        return True
    elif type == "latte" and water>=200 and milk>=150 and coffee>=24:
        print("There is enough resources")
        return True
    elif type == "cappuccino" and water>=250 and milk>=100 and coffee>=24:
        print("There is enough resources")
        return True
    else:
        return False

def check_enough(type,quarters,dimes,nickels,pennies):
    total = (quarters*.25) + (dimes*.1) + (nickels*.05) + (pennies*.01)
    if type == "espresso" and total >= 1.5:
        print(f"Here is your change {total-1.5}")
        return True
    elif type == "latte" and total >= 2.5:
        print(f"Here is your change {total-2.5}")
        return True
    elif type == "cappuccino" and total >= 3:
        print(f"Here is your change {total-3}")
        return True
    else:
        print('That is not enough money. You have been refunded.')
        return Falsew



while True:
    user_input = input("What would you like (espresso/latte/cappuccino)\n")

    if user_input == "off":
        break
    elif user_input == "report":
        print(f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}")
    else:
        enough = check_resources(user_input)
        if enough == True:
            print("Please enter coins")
            quarters = int(input("Number of quarters\n"))
            dimes = int(input("Number of dimes\n"))
            nickels = int(input("Number of nickels\n"))
            pennies = int(input("Number of pennies\n"))
            should_do = check_enough(user_input,quarters,dimes,nickels,pennies)
            if should_do==True:
                if user_input=="espresso":
                    money +=1.5
                    water -= 50
                    coffee -=18
                elif user_input=="latte":
                    money +=2.5
                    water -= 200
                    milk -=150
                    coffee -=24
                elif user_input=="cappuccino":
                    money +=3
                    water -= 250
                    milk -=100
                    coffee -=24
                print(f"Here is you {user_input}. Enjoy!")
                print(f"Here is the money {money}")
        else:
            print("Sorry there is not enough resources")
