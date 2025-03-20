from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    user_input = input(f"What would you like to order {menu.get_items()}\n")
    if user_input=="off":
        break
    elif user_input=="report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_input)
        is_enough = coffee_maker.is_resource_sufficient(drink)
        if is_enough == True:
            print("There is enough resources")
            money_accepted = money_machine.make_payment(drink.cost)
            if money_accepted==True:
                print("You have paid")
                coffee_maker.make_coffee(drink)
                coffee_maker.report()
                money_machine.report()

    