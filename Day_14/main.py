MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report():
    """Prints the current resources."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")

def coffee_type(coffee_name):
    """Returns the required ingredients for the chosen coffee."""
    if coffee_name in MENU:
        ingredients = MENU[coffee_name]["ingredients"]
        return ingredients["water"], ingredients["milk"], ingredients["coffee"]
    else:
        print("Invalid coffee type.")
        return None

def resources_sufficient(water_needed, milk_needed, coffee_needed):
    """Checks if resources are sufficient for the drink."""
    if resources["water"] < water_needed:
        print("Sorry, not enough water.")
        return False
    if resources["milk"] < milk_needed:
        print("Sorry, not enough milk.")
        return False
    if resources["coffee"] < coffee_needed:
        print("Sorry, not enough coffee.")
        return False
    return True

def deduct_resources(water_used, milk_used, coffee_used):
    """Deducts the used ingredients from the resources."""
    resources["water"] -= water_used
    resources["milk"] -= milk_used
    resources["coffee"] -= coffee_used

def insert_coins(cost):
    """Processes the coins inserted and returns True if payment is successful."""
    print("Please insert coins:")
    try:
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
    except ValueError:
        print("Invalid coin input. Try again.")
        return False

    total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies
    total = round(total, 2)

    if total < cost:
        print(f"Sorry, that's not enough money. ${total} refunded.")
        return False
    change = round(total - cost, 2)
    if change > 0:
        print(f"Here is ${change} in change.")
    return True

def order():
    profit = 0
    while True:
        command = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

        if command == "off":
            print("Shutting down. Goodbye!")
            break
        elif command == "report":
            report()
        elif command in MENU:
            water_needed, milk_needed, coffee_needed = coffee_type(command)

            if resources_sufficient(water_needed, milk_needed, coffee_needed):
                cost = MENU[command]["cost"]
                if insert_coins(cost):
                    deduct_resources(water_needed, milk_needed, coffee_needed)
                    profit += cost
                    print(f"Here is your {command} ☕ Enjoy!")
        else:
            print("Invalid command. Try espresso, latte, cappuccino, report, or off.")

    print(f"Total profit: ${profit}")

# Run the coffee machine
order()
