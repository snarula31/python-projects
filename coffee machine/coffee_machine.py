import os
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

profit = 0
resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}

os.system('cls')


def is_resources_sufficient(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry ther is not enough {item}")
            return False
    return True


def process_coins():
    print("Insert coins.")
    total = int(input("how many quaters?($0.25): ")) * 0.25
    total += int(input("how many dimes?($0.1):")) * 0.1
    total += int(input("how many nickels?($0.05):")) * 0.05
    total += int(input("how many pennies?($0.01)")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += money_received - change
        return True
    else:
        print("Sorry not enough money. Money refunded.")
        return False


def make_coffe(drink_name, order_ingredients):
    for items in resources:
        resources[items] -= order_ingredients[items]
    print(f"Here is your {drink_name}")


is_on = True

while is_on:

    print("****Main Menu*****")
    for kv in MENU:  # print types of coffees available in a new line each
        print(kv)
    print("report")
    print("off")
    choice = input("What would you like?:")
    os.system('cls')
    print(f"You seleted {choice}")
    if choice == 'off':
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {profit}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink['ingredients']):
            print("Cost: $", drink["cost"])
            payment = process_coins()
            is_transaction_successful(payment, drink["cost"])
            make_coffe(choice, drink["ingredients"])
