from tkinter import Menu

insert_coins = []

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


def choice(client_choice):
    global coffee_amount, water_amount, milk_amount, coffee_cost
    print(f"{client_choice}")
    if client_choice == "espresso" or "latte" or "cappuccino":
        water_amount = MENU[client_choice]["ingredients"]["water_amount"]
        coffee_amount = MENU[client_choice]["ingredients"]["coffee_amount"]
        if client_choice == "espresso":
            milk_amount = 0
        else:
            milk_amount = MENU[client_choice]["ingredients"]["milk_amount"]
        coffee_cost = MENU[client_choice]["coffee_cost"]
        print(f"Water: {water_amount}ml\nCoffee: {coffee_amount}g\nMilk: {milk_amount}ml\nMoney: ${coffee_cost}\n")
    else:
        print ("Invalid choice")
        print(MENU)

    return client_choice, water_amount, coffee_amount, milk_amount, coffee_cost


state = False
while not state:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    user_choice, water, coffee, milk, cost = choice(user_choice)
   
    remaining_water = resources["water"] = resources["water"] - water
    remaining_coffee = resources["coffee"] = resources["coffee"] - coffee
    remaining_milk = resources["milk"] = resources["milk"] - milk

    if remaining_water >= 0 and remaining_coffee >= 0 and remaining_milk >= 0:
        quarters = 0.25
        dimes = 0.10
        pennies = 0.01
        number = 0
        sum_coins = 0
        
        while sum_coins < cost:
            insert_coins = int(input("Insert coins: Type 1 for dollar, 2 for quarter, 3 for dime, 4 for penny: "))
            
            if insert_coins == 1:
                dollar = int(input("How many dollars? "))
                dollar = dollar * 1
            elif insert_coins == 2:
                number_quarters = int(input("How many quarters? "))
                quarters = number_quarters * 0.25
            elif insert_coins == 3:
                number_dimes = int(input("How many dimes? "))
                dimes = number_dimes * 0.10
            elif insert_coins == 4:
                number_penny = int(input("How many pennies? "))
                pennies = number_penny * 0.01
            else:
                print("Invalid coin")
                break
            sum_coins = dollar + quarters + dimes + pennies
            
        print(f"Inserted: ${sum_coins}, Remaining: ${cost - sum_coins}")

    if remaining_water - water < 0:
        print("Sorry, not enough water!")
    elif remaining_coffee - coffee < 0:
        print("Sorry, not enough coffee!")
    elif remaining_milk - milk  < 0:
        print("Sorry, not enough milk!")
    
    print(f"Remaining water: {remaining_water}ml\nRemaining coffee: {remaining_coffee}g\nRemaining milk: {remaining_milk}ml\n")