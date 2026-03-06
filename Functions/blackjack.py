import random
import blackjack_art

def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card


def calculate_score(cards):
    # Take the list of cards and calculate the score calculated from the cards
    if sum(cards)==21 and len(cards)==2:
        return 21
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def playGame():
    user_card=[]
    comp_card=[]
    is_game_over=False
    user_score=-1
    computer_score=-1

    for _ in range(2):
        user_card.append(deal_card())
        comp_card.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(comp_card)

        print(f"Your cards: {user_card}, current score: {user_score}")
        print(f"Computer first card: {comp_card[0]}")

        if user_score==21 or computer_score==21 or user_score >21:
            is_game_over=True
        else:
            another_card=input("Do you want to get another card? y or n")
            if another_card=="y":
                user_card.append(deal_card())
            else:
                is_game_over=True


    while computer_score<17:
        comp_card.append(deal_card())
        computer_score = calculate_score(comp_card)

    print(f"computer cards are : {comp_card}")

    def compare(userScore,computerScore):
        if userScore==computerScore:
            return "Draw"
        elif computerScore==21:
            return "Loose opponent has blackjack"
        elif userScore==21:
            return "Win with a blackjack"
        elif userScore>21:
            return "You went over you loose"
        elif computerScore>21:
            return "Opponent went over you win"
        elif userScore>computerScore:
            return "You Win"
        else:
            return "You Loose"

    print(compare(user_score,computer_score))


while input("Do you want to play a game Blackjack? y or n") == "y":
    print("\n" * 20)
    print(blackjack_art.logo)
    playGame()