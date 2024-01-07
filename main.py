MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    "money": 0
}


def get_suffix_ingredients(ingredient):
    if ingredient == 'water' or ingredient == 'milk':
        return 'ml'
    elif ingredient == 'coffee':
        return 'g'
    else:
        return "$"


def printReport():
    """Print resources of machine"""
    for key in resources.keys():
        print(f"{key}: {resources[key]}{get_suffix_ingredients(key)}")


def check_resources(coffee_name):
    """Check resources of machine for making coffee """
    coffee = MENU[coffee_name]
    insufficient_message = "Sorry there is not enough"
    ingredients = coffee["ingredients"].keys()
    for ingredient in ingredients:
        if resources[ingredient] < coffee["ingredients"][ingredient]:
            insufficient_message += f" {ingredient}."
            print(insufficient_message)
            return False
    return True


def get_paid(coffee_name):
    """Get paid for Coffee"""
    coffee_cost = MENU[coffee_name]['cost']
    print("Please insert coins.")
    quarters = int(input("how many quarters? "))
    dimes = int(input("how many dimes? "))
    pennies = int(input("how many pennies? "))
    nickels = int(input("how many nickels? "))
    total_paid_amount = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    if total_paid_amount >= coffee_cost:
        remain = round(total_paid_amount - coffee_cost, 2)
        print(f"Here is ${remain} in change.")
        resources["money"] = resources['money'] + coffee_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(coffee_name):
    paid = get_paid(coffee_name)
    if paid:
        coffee = MENU[coffee_name]
        ingredients = coffee["ingredients"].keys()
        for ingredient in ingredients:
            resources[ingredient] = resources[ingredient] - coffee["ingredients"][ingredient]
        print(f"Here is your {coffee_name} ☕️. Enjoy!")


def on():
    is_on = True
    while is_on:
        coffee_name = input("Would you like? (espresso/latte/cappuccino): ")
        if coffee_name == "report":
            printReport()
        elif coffee_name == "off":
            is_on = False
        elif coffee_name in MENU.keys():
            has_resources = check_resources(coffee_name)
            if has_resources:
                make_coffee(coffee_name)
        else:
            print("Invalid input entered")


on()
