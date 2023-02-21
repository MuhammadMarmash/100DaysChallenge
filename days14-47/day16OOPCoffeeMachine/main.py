from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
coffee = CoffeeMaker()
menu = Menu()
money = MoneyMachine()
while True:
    order_name = str(input(f"What would you like? ({menu.get_items()}):")).lower()
    if order_name == "report":
        coffee.report()
        money.report()
    elif order_name == 'off':
        is_on = False
    else:
        if menu.find_drink(order_name) is None:
            print("please select an available coffee")
        elif coffee.is_resource_sufficient(menu.find_drink(order_name)):
            if money.make_payment(menu.find_drink(order_name).cost):
                coffee.make_coffee(menu.find_drink(order_name))
