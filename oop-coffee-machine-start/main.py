from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
Making_coffee = True
my_menu = Menu()
coffee_machine = CoffeeMaker()
coin_dispenser = MoneyMachine()
while Making_coffee:
    drink_ordered = input(f"What would you like? (latte,espresso,cappuccino)")
    if drink_ordered == "off":
        Making_coffee = False
    elif drink_ordered == "report":
        coffee_machine.report()
        coin_dispenser.report()
    else:
        item = my_menu.find_drink(drink_ordered)
        available = coffee_machine.is_resource_sufficient(item)
        if available:
            transaction = (coin_dispenser.make_payment(item.cost))
            if transaction:
                (coffee_machine.make_coffee(item))



