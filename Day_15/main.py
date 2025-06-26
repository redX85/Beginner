from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Treat the code as though it's an external library
# I really don't know how to do this project: I'll look at how she does the project

# TODO 1: Print report
# We don't have to care about how the called functions work
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
coffee_maker.report()
money_machine.report()

# TODO 2: Check resource sufficient
is_on = True
menu = Menu()
while is_on:
    try:
        options = menu.get_items()
        choice = str(input(f"What would you like? {options}: "))
        if choice == "off":
            is_on = False
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink):
                # TODO 3: Process coins
                # TODO 4: Check transaction successful
                if money_machine.make_payment(drink.cost):
                    # TODO 5: Make coffee
                    coffee_maker.make_coffee(drink)
    except AttributeError:
        print("Please add either of the options provided.")
