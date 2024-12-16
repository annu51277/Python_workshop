from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

M = Menu()
MI = MenuItem
CM = CoffeeMaker()
MM = MoneyMachine()


# print(M.get_items())
#
# M.find_drink('latte')
is_on = True


while is_on:
    print("Welcome to Coffe Shop:")
    u_choice = input(f"What would you like? {M.get_items()}: ")
    drink = M.find_drink(u_choice)
    resources = CM.is_resource_sufficient(drink)
    report = input("Do you want to check inventory?: ").lower()
    if report == 'y' or report == 'yes':
        CM.report()
    if resources:

        print(f"The cost of {u_choice} is {drink.cost}")
        print("Insert coins quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01")
        if MM.make_payment(drink.cost):
            CM.make_coffee(drink)
    else:
        print(f"The coffee machine do not have required resources for {u_choice}: ")
        secret_code = input("Enter code to turn off the machine").lower()
        if secret_code == 'off':
            print("Turning off Machine")
            is_on = False
        else:
            continue

        # CM.report()




