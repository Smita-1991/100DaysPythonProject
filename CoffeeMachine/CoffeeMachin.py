#TODO: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
import Menu
dispensed=True
water=Menu.resources["water"]
milk=Menu.resources["milk"]
coffee=Menu.resources["coffee"]
profit=0

def turnOffCoffeeMachine():
    print(input("off"))

def printReport(used_water,used_milk,used_coffee,spend_money):
    print(f"Water: {used_water} \nMilk: {used_milk} \nCoffee: {used_coffee} \nMoney: ${spend_money}")

def checkTransaction(drink,totalBill):
    global profit
    print("insert coins")
    if totalBill>= Menu.MENU[drink]["cost"] :
        change=totalBill-Menu.MENU[drink]["cost"]
        print(f"Here is ${change} dollars in change.")
        profit=Menu.MENU[drink]["cost"]
        print(f"report after purchasing {drink}")
        printReport(water,milk,coffee,profit)
        print(f"Here is your {drink}. Enjoy!")

def isResourceSufficient(drink):
    for item in drink:
        if drink[item] >= Menu.resources[item]:
            print(f"there is not enough {item}.")
            return False
    return True

def checkResourcesSufficient(drink):
    milkRequired = 0
    global water,milk,coffee

    if drink == 'latte' or  drink=='cappuccino':
        milkRequired = Menu.MENU[drink]["ingredients"]["milk"]
    waterRequired=Menu.MENU[drink]["ingredients"]["water"]
    coffeRequired=Menu.MENU[drink]["ingredients"]["coffee"]

    totalBill = 0
    totalBill += int(input("How many quarter?")) * 0.25
    totalBill += int(input("How many dime?")) * 0.1
    totalBill += int(input("How many nickle?")) * 0.05
    totalBill += int(input("How many pennies?")) * 0.01
    if totalBill < Menu.MENU[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    else:
        water -= waterRequired
        milk -= milkRequired
        coffee -= coffeRequired
        checkTransaction(drink,totalBill)


while dispensed:
    choice=input("What would you like? (espresso/latte/cappuccino):")
    if choice == 'off':
        dispensed=False
    elif choice == 'report':
        print(f"Water: {water} \nMilk: {milk} \nCoffee: {coffee} \nMoney:${profit}")
    else:
        if isResourceSufficient(Menu.MENU[choice]["ingredients"]):
            checkResourcesSufficient(choice)