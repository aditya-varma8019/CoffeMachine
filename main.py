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
}

money = 0


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


# def check_resources_sufficient(user_input):

def process_coins():
    pen = int(input("Enter the number of pennies: "))
    nic = int(input("Enter the number of dimes: "))
    dim = int(input("Enter the number of nickles: "))
    qua = int(input("Enter the number of quarters: "))
    total_amount = pen*0.01 + nic*0.05 + dim*0.1 + qua*0.25
    return total_amount


is_off = False
while not is_off:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "off":
        is_off = True
        continue

    elif user_input == "report":
        print_report()
        continue

    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        is_possible = True
        not_sufficient_resource = ""
        for key in MENU[user_input]["ingredients"]:
            if resources[key] < MENU[user_input]["ingredients"][key]:
                is_possible = False
                not_sufficient_resource = key
                break

        if not is_possible:
            print(f"Sorry there is not enough {not_sufficient_resource}")
            continue

    else:
        print("Please enter correct input!!")
        continue

    is_transaction_successful = True
    print("Insert coins: ")
    user_given_amount = process_coins()
    if MENU[user_input]["cost"] > user_given_amount:
        print("Sorry that's not enough money. Money refunded.")
        is_transaction_successful = False
        continue

    money += MENU[user_input]["cost"]
    for key in MENU[user_input]["ingredients"]:
        resources[key] -= MENU[user_input]["ingredients"][key]

    change = round(user_given_amount-MENU[user_input]["cost"], 2)
    print(f"Here is ${change} dollars in change.")

    print(f"“Here is your {user_input} ☕. Enjoy!")

print("Coffee Machine is now off!!")
