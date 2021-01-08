from machine import menu, resources


def update_resources(next_drink):
    """updates the ingredient amount after each order"""
    for ingredient in menu[next_drink]["ingredients"]:
      resources[ingredient] -= menu[next_drink]["ingredients"][ingredient]


def check_resources(next_drink):
    """Returns True if there sufficient resources, otherwise, returns false."""
    for ingredient in menu[next_drink]["ingredients"]:
        if resources[ingredient] < menu[next_drink]["ingredients"][ingredient]:
            print(f"Sorry, there is not enough {ingredient}...")
            return False
    return True


def money():
    """Returns total coins inserted by the user."""
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))*0.25
    dimes = int(input("How many dimes? "))*0.1
    nickles = int(input("How many nickles? "))*0.05
    pennies = int(input("How many pennies? "))*0.01
    total = quarters + dimes + nickles + pennies
    return total


def check_money(next_drink, payment):
    """Compares the inserted coins and cost of the drink, returns true if coins are enough and false if not enough money"""
    if menu[next_drink]["cost"] > payment:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif menu[next_drink]["cost"] < payment:
        refund = payment - menu[next_drink]["cost"]
        print("Here is ${:0.2f} in change...".format(refund))
    else:
        resources["Money"] = menu[next_drink]["cost"]
    return True

#loop to run the coffee maker
machine = True
while machine:
    next_drink = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if next_drink == "off":
        machine = False
    elif next_drink == "report":
        for item in resources:
            print(f"{item}: {resources[item]}")
    else:
        if check_resources(next_drink):
            payment = money()
            if check_money(next_drink, payment):
                update_resources(next_drink)
                print(f"Here is your {next_drink}. Enjoy!")