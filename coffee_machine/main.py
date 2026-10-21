import coffes
def resources():
    print("water: " + str(coffes.resources["water"]))
    print("coffee: " + str(coffes.resources["coffee"]))
    print("milk: " + str(coffes.resources["milk"]))
    print("money: " + str(coffes.resources["money"]))
def check_resources(drink):
    if coffes.MENU[drink]["ingredients"]["water"] > coffes.resources["water"]:
        print("Sorry, you don't have enough water")
        return False

    elif coffes.MENU[drink]["ingredients"]["coffee"] > coffes.resources["coffee"]:
         print("Sorry, you don't have enough coffee")
         return False
    elif coffes.MENU[drink]["ingredients"]["milk"] > coffes.resources["milk"]:
        print("Sorry, you don't have enough milk")
        return False
    else:
        return True

def payment(quarter, dime, nickel, penny):
    dollars = 0.00
    for dollar in range(quarter):
        dollars += 0.25
    for dollar in range(dime):
        dollars += 0.10
    for dollar in range(nickel):
        dollars += 0.05
    for dollar in range(penny):
        dollars += 0.01
    return round(dollars , 2)
def payment_check(money, drink):
    change = 0.00
    if money < coffes.MENU[drink]["cost"]:
        print("Sorry, you don't have enough money")
        return False
    elif money == coffes.MENU[drink]["cost"]:
        return True
    else:
        change =round(money - coffes.MENU[drink]["cost"], 2)
        print(f"Here is your change: ${change}")
        return True





def machine():
    using_machine = True
    while using_machine:
        selected_option = input("What would you like (latte, espresso, cappuccino)").lower()
        if selected_option == "off":
            return
        if selected_option == "report":
            resources()
        if selected_option == "latte" or selected_option == "espresso" or selected_option == "cappuccino":
            resources_available = check_resources(selected_option)
            if resources_available:
                print("Please insert coins.")
                quarters = int(input("Quarters: "))
                dimes = int(input("Dimes: "))
                nickels = int(input("Nickels: "))
                pennies = int(input("Pennies: "))
                verified_payment = payment_check(payment(quarters, dimes, nickels, pennies), selected_option)
                if verified_payment:
                    coffes.resources["money"] += coffes.MENU[selected_option]["cost"]
                    coffes.resources["water"] -= coffes.MENU[selected_option]["ingredients"]["water"]
                    coffes.resources["coffee"] -= coffes.MENU[selected_option]["ingredients"]["coffee"]
                    coffes.resources["milk"] -= coffes.MENU[selected_option]["ingredients"]["milk"]
                    print(f"Here is your {selected_option} enjoy!")


machine()


