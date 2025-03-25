
import art
import random


def userFinalScore():
    return user_initial_score+random.choice(card_list)

def computerFinalScore():
    return computer_first_card+random.choice(card_list)

def checkComputerScore(user_Score,computer_score):
    final_computer_score=computer_score
    computer_new_card = random.choice(card_list)
    if final_computer_score <= 16:
        while final_computer_score < 16:
            final_computer_score +=computer_new_card
        if final_computer_score > 21:
            print("User win")
        else:
            if user_Score > final_computer_score:
                print("User win")
            elif user_Score==final_computer_score:
                print("Draw")
            else:
                print("Computer win")
    else:
        if user_Score > final_computer_score:
            print("User win")
        elif user_Score == final_computer_score:
            print("Draw")
        else:
            print("Computer win")



def check_blackjack(user_score):
    if user_score == 21:
        print("user Win")
    elif computer_first_card == 21:
        print("Computer win")
    else:
        if user_score > 21:
            if  user_first_card == 11 :
                if 1+user_second_card>21:
                    print("User loose")
            elif user_second_card ==11:
                if user_first_card+1>21:
                    print("User loose")
                else:
                    print("User Win with a Blackjack")
            else:
                print("User loose")
        else:
            choice = input("Type 'y' to get another card, type 'n' to pass:")
            if choice == 'y':
                # newRandomNumber = random.choice(card_list)
                # user_score = sum([user_first_card, user_second_card, newRandomNumber])
                # print(f"Your cards: {}, current score: {user_score}")

                check_blackjack(user_score+random.choice(card_list))
            else:
                checkComputerScore(user_score, computer_first_card)

# def userScore():
#     user_initial_score=user_first_card + user_second_card
#     return user_initial_score+random.choice(card_list)
#
# def computerScore(computerRandomCard):
#     return computer_first_card+computerRandomCard
card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_cards():
    card=random.choice(card_list)
    return card

user_initial_score=[]
computer_cards=[]

for i in range(2):
    new_card=[deal_cards()]
    user_initial_score.append(new_card)

def calculateScore(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    elif 11 in cards and sum(cards)>21:








print(art.calculator)
print(f"Your cards : [{user_first_card,user_second_card}]")
print(f"current score: {sum([user_first_card,user_second_card])} ")

user_initial_score=sum([user_first_card,user_second_card])

computer_first_card = random.choice(card_list)
print(f"Computer's first card: {computer_first_card}")

choice=input("Type 'y' to get another card,type 'n' to pass:")
if choice=='y':
    randomNumber=random.choice(card_list)
    user_initial_score=sum([user_first_card,user_second_card,randomNumber])
    print(f"Your final hand: {user_first_card,user_second_card,randomNumber} final score: {user_initial_score}")
    check_blackjack(user_initial_score)
else:
    checkComputerScore(user_initial_score,computer_first_card)



