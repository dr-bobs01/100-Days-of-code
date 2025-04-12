from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money = MoneyMachine()
coffee = CoffeeMaker()
menu = Menu()

# print(menu.get_items())

on = True
while on:
    request = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if request == "report":
        coffee.report()
        money.report()
    elif request == "off":
        exit()
    # do a bunch of checks if you have enough resources
    temp = menu.find_drink(request)
    if temp is not None:
        if coffee.is_resource_sufficient(temp):
            if money.make_payment(temp.cost):
                coffee.make_coffee(temp)
