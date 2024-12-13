print("Welcome to python pizza deliveries!")
size=input("What size pizza do you want? s, M  or L: ")
pepperoni=input("Do you want pepperoni on your pizza? Y or N")
extra_Cheese=input("Do you want extra cheese on your pizza? Y or N")
total_bill=0
if size=="S":
    total_bill=15
    if pepperoni=="Y":
        total_bill+=2
    if extra_Cheese =="Y":
        total_bill+=1
    print(f"Your final bill is: ${total_bill}")

elif size=="M":
    total_bill = 20
    if pepperoni=="Y":
        total_bill+=3
    if extra_Cheese:
        total_bill+=1
    print(f"Your final bill is: ${total_bill}")

elif size=="L":
    total_bill = 25
    if pepperoni=="Y":
        total_bill+=3
    if extra_Cheese:
        total_bill+=1
    print(f"Your final bill is: ${total_bill}")

else:
    print("You typed the wrong input")
