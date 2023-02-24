from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
cfeMkr = CoffeeMaker()
mnyMachine = MoneyMachine()


def main():
    is_on = True
    while is_on:
        choice = input(f"What would you like? {menu.get_items()} : ")
        if choice == "off":
            print("Goodbye")
            is_on = False
        elif choice == "report":
            cfeMkr.report()
            mnyMachine.report()
        else:
            drink = menu.find_drink(choice)
            if cfeMkr.is_resource_sufficient(drink):
                if mnyMachine.make_payment(drink.cost):
                    cfeMkr.make_coffee(drink)

if __name__ == "__main__":
    main()
        
        