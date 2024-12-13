print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`.".` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to the treasure Island")
print("Your mission is to find the treasure")
direction_1=input("You are at the cross road. Where do you want to go? Type Left or Right\n")
if direction_1=="Left":
    direction_2=input('''You've come to lake. There is an Island in the middle of the lake.
            Type Wait to wait for a Boat. Type Swim to swim across''')
    if direction_2=="Wait":
        direction_3=input("Which color of door do you want to choose? Red, Blue or Yellow")
        if direction_3=="Yellow":
            print("You are win")
        elif direction_3=="Red":
            print("Burned by fire.Game Over")
        elif direction_3=="Blue":
            print("Eaten by beasts.Game Over.")
        else:
            print("Game over")

    else:
        print("Attacked by trout.Game Over.")
else:
    print("Fall into a hole.Game Over.")


