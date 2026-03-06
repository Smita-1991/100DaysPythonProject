import random

difficulty_type=input("Choose a difficulty. Type 'easy' or 'hard'")
attempts=0
if difficulty_type=='easy':
    attempts=10
else:
    attempts=5
random_number = random.randint(1, 100)
print(random_number)
while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    user_number = int(input("Make a guess.\n"))

    if user_number == random_number:
        print(f"You got it right! The number was {user_number}.")
        exit()
    elif user_number<random_number:
        print("Too low")
        attempts-=1
    elif user_number>random_number:
        print("Too high")
        attempts-=1
    else:
        print("You have run out of guesses you lose")
if attempts==0:
    print("You have run out of guesses you lose")

