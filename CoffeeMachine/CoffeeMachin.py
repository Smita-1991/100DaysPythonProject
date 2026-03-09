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

def checkTransaction(money,drink):
    global profit
    if money> Menu.MENU[drink]["cost"]:
        change=money-Menu.MENU[drink]["cost"]
        print(f"Here is ${change} dollars in change.")

    profit=Menu.MENU[drink]["cost"]
    print(f"report after purchasing {drink}")
    printReport(water,milk,coffee,profit)
    print(f"Here is your {drink}. Enjoy!")

def checkResourcesSufficient(drink):
    waterRequired = 0
    milkRequired = 0
    coffeRequired = 0
    global water,milk,coffee

    if drink == 'espresso':
        waterRequired=Menu.MENU[drink]["ingredients"]["water"]
        coffeRequired=Menu.MENU[drink]["ingredients"]["coffee"]
    elif drink == 'latte':
        waterRequired = Menu.MENU[drink]["ingredients"]["water"]
        milkRequired = Menu.MENU[drink]["ingredients"]["milk"]
        coffeRequired=Menu.MENU[drink]["ingredients"]["coffee"]
    elif drink == 'cappuccino':
        waterRequired = Menu.MENU[drink]["ingredients"]["water"]
        milkRequired = Menu.MENU[drink]["ingredients"]["milk"]
        coffeRequired = Menu.MENU[drink]["ingredients"]["coffee"]

    if water < waterRequired:
        print("there is not enough water.")
    elif milk < milkRequired:
        print("there is not enough milk.")
    elif coffee < coffeRequired:
        print("there is not enough coffee.")
    else:
        print("insert coins")
        totalBill=0
        totalBill += int(input("quarter")) * 0.25
        totalBill += int(input("dime")) * 0.1
        totalBill += int(input("nickle")) * 0.05
        totalBill += int(input("pennies")) * 0.01
        if totalBill < Menu.MENU[drink]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
            printReport(water, milk, coffee, Menu.MENU[drink]["cost"])
        water -= waterRequired
        milk -= milkRequired
        coffee -= coffeRequired

        checkTransaction(totalBill,drink)

while dispensed:
    choice=input("What would you like? (espresso/latte/cappuccino):")
    if choice == 'off':
        exit()

    print(f"report before purchasing {choice}")
    print(f"Water: {water} \nMilk: {milk} \nCoffee: {coffee} \nMoney: $0")
    checkResourcesSufficient(choice)