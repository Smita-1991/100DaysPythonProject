import random

import HigherLowerArt
import HigherLowerGame_data

print(HigherLowerArt.logo)
currentScore=0
firstPlayer=0
secondPlayer=0

should_continue=True
def getName(index):
    return HigherLowerGame_data.data[index]["name"]

def getFollowerCount(index):
    return HigherLowerGame_data.data[index]["follower_count"]

def getDescription(index):
    return HigherLowerGame_data.data[index]["description"]

def getCountry(index):
    return HigherLowerGame_data.data[index]["country"]

def compare_score(guessedPlayer,first_player, second_player,current_score):
    global firstPlayer,should_continue,currentScore
    print("\n" * 20)
    print(HigherLowerArt.logo)
    if guessedPlayer=='A' and getFollowerCount(first_player) > getFollowerCount(second_player):
        current_score+=1
        currentScore=current_score
        print(f"You are right! current score : {currentScore}")
    elif guessedPlayer=='B' and getFollowerCount(second_player) > getFollowerCount(first_player):
        current_score+=1
        currentScore=current_score
        print(f"You are right! current score : {currentScore}")
        firstPlayer=second_player
    else:
        print(f"Sorry, that's wrong. Final score : {currentScore} ")
        should_continue=False


while should_continue:
    print(f"Compare A: {getName(firstPlayer)}, {getFollowerCount(firstPlayer)} from {getCountry(firstPlayer)}\n")
    print(f"{HigherLowerArt.vs}\n")
    randomPlayer=random.choice([ele for ele in HigherLowerGame_data.data if ele!=firstPlayer])
    secondPlayer=HigherLowerGame_data.data.index(randomPlayer)
    print(f"Against B: {getName(secondPlayer)}, {getDescription(secondPlayer)} from {getCountry(secondPlayer)}\n")
    guessPlayer=input("Who has more followers? Type 'A' or 'B':")
    compare_score(guessPlayer,firstPlayer, secondPlayer,currentScore)

