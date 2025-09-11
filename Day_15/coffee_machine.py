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

def generate_report() :
    for item in resources:
        print(f"{item}: {resources[item]}{'ml' if item == 'water' or item == 'milk' else 'g'}")
    print(f"Money: ${money}")


def check_resources_sufficient(water, milk, coffee) :
    if water > resources["water"] :
        print("Water is not sufficient")
        return False
    elif milk > resources["milk"] :
        print("Milk is not sufficient")
        return False
    elif coffee > resources["coffee"]:
        print("Coffe is not sufficient!")
        return False
    return True

def insert_coins(coffee_cost):
    global money
    quarters = int(input("How many Quarters : ")) * 0.25
    dimes = int(input("How many Dimes : ")) * 0.10
    nickles = int(input("How many Nickels : ")) * 0.05
    penny = int( input("How many Pennies : ")) * 0.01
    total = quarters + dimes + nickles + penny

    if total < coffee_cost :
        print("Amount is not sufficient")
        return False
    else :
        remains = total - coffee_cost
        money += coffee_cost
        print(f"Here is ${remains} in change")
        return True


def update_machine(water, milk, coffee) :
    resources["milk"] -= milk
    resources["water"] -= water
    resources["coffee"] -= coffee

make_coffee = True

while make_coffee :
    users_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if users_choice not in MENU :
        if users_choice != 'report' :
            print("Invalid User Input! ")
            continue

    if users_choice == 'report' :
        generate_report()
    elif users_choice == 'exit' :
        break
    else :
        water = MENU[users_choice]['ingredients'].get("water", 0)
        milk = MENU[users_choice]['ingredients'].get("milk", 0)
        coffee = MENU[users_choice]['ingredients'].get("coffee", 0)

        if check_resources_sufficient(water, milk, coffee):
            is_able_to_buy = insert_coins(MENU[users_choice]["cost"])
            if is_able_to_buy:
                update_machine(water, milk, coffee)
                print(f"Here is your {users_choice} Enjoy!")