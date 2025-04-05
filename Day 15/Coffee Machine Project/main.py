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
    "money": 0,
}

def report():
    print(f"""Water: {resources["water"]}ml
Milk: {resources["milk"]}ml
Coffee: {resources["coffee"]}g
Money: ${resources["money"]}""")

def res_check():
    if MENU[request]["ingredients"]["water"] < resources["water"]:
        try:
            if MENU[request]["ingredients"]["milk"] < resources["milk"]:
                if MENU[request]["ingredients"]["coffee"] < resources["coffee"]:
                    return True
            else:
                return "milk"
        except KeyError:
            if MENU[request]["ingredients"]["coffee"] < resources["coffee"]:
                return True
        else:
            return "coffee"
    else:
        return "water"

def money():
    print("Please insert coins.")
    q = int(input("How many quarters?: "))
    d = int(input("How many dimes?: "))
    n = int(input("How many nickles?: "))
    p = int(input("How many pennies?: "))
    change = (MENU[request]["cost"]-(q * 0.25)-(d * 0.10)-(n*0.05)-(p*0.01))
    if change <= 0:
        print(f"Here is ${round(change * -1,2)} in change.")
        resources["water"] -= MENU[request]["ingredients"]["water"]
        try:
            resources["milk"] -= MENU[request]["ingredients"]["milk"]
        except KeyError:
            5 + 5 # i needed a line of code that did nothing for the code to work
        resources["coffee"] -= MENU[request]["ingredients"]["coffee"]
        resources["money"] += MENU[request]["cost"]
        print(f"Here is your {request} ☕️. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")

on = True
while on:
    request = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if request == "report":
        report()
    elif request == "off":
        exit()
    ## do a bunch of checks if you have enough resources
    if request in MENU:
        temp = res_check()
        if temp == True:
            ## this is where money check goes
            money()
        else:
            print(f"Sorry there is not enough {temp}.")
