# Rock Paper Scissors ASCII Art

import random

Rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

Scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

yourChoice=int(input("What do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors.\n"))
if yourChoice==0:
    print(Rock)
elif yourChoice==1:
    print(Paper)
elif yourChoice==2:
    print(Scissors)
else:
    print("You Entered incorrect number")

print("Computer choose:")
randomNumber=random.randint(0, 2)
if randomNumber==0:
    print(Rock)
elif randomNumber==1:
    print(Paper)
else:
    print(Scissors)

if yourChoice== randomNumber:
    print("Neutral")
elif yourChoice==0 and randomNumber==2:
    print("You Wins!")
elif yourChoice==1 and randomNumber==0:
    print("You Win!")
elif yourChoice==2 and randomNumber==1:
    print("You Win!")
elif yourChoice>2:
    print("You Entered incorrect number")
else:
    print("You loose!")