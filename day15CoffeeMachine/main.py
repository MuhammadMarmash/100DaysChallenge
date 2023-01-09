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
money_earned = 0
is_on = True
while True:

    order = str(input(f"What would you like? (espresso {MENU['espresso']['cost']}/latte {MENU['latte']['cost']}"
                      f"/cappuccino {MENU['cappuccino']['cost']}):")).lower()
    if order == "report":
        print(f"""Water: {resources['water']}ml
Milk: {resources['milk']}ml
Coffee: {resources['coffee']}g
Money: {money_earned}$""")
    elif order == 'off':
        is_on = False
    else:
        ingredients = MENU[order]['ingredients']
        water_check = resources['water'] > ingredients['water']
        if order != "espresso":
            milk_check = resources['milk'] > ingredients['milk']
        else:
            milk_check = True
        coffee_check = resources['coffee'] > ingredients['coffee']
        if water_check and milk_check and coffee_check:
            print("Please insert coins.")
            quarters = int(input("how many quarters?:"))  # 0.25
            dimes = int(input("how many dimes?:"))  # 0.1
            nickles = int(input("how many nickles?:"))  # 0.05
            pennies = int(input("how many pennies?:"))  # 0.01
            payment = (quarters*0.25)+(dimes*0.1)+(nickles*0.05)+(pennies*0.01)
            if payment > MENU[order]['cost']:
                change = round(payment - MENU[order]['cost'], 2)
                print(f"Here is {change}$ in change.")
                print(f"Here is your {order} ☕️. Enjoy!")
                money_earned += MENU[order]['cost']
                resources['water'] -= ingredients['water']
                if order != "espresso":
                    resources['milk'] -= ingredients['milk']
                resources['coffee'] -= ingredients['coffee']
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            if not water_check:
                print("Sorry there is not enough water.")
            if not milk_check:
                print("Sorry there is not enough milk.")
            if not coffee_check:
                print("Sorry there is not enough coffee.")
