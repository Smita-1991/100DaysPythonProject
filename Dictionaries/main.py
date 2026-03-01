import art

print(art.logo)

name = input("What's your name?")
bidding_value=input("What's your Bid?")

bidder_info= {name: bidding_value}

print(bidder_info)

def findHighestBidder(bidding_dictionary):
    winner=""
    highestBid=0
    for bidder in bidding_dictionary:
        bidAmount=int(bidding_dictionary[bidder])
        if bidAmount>highestBid:
            highestBid=bidAmount
            winner=bidder
    print(f"The winner is {winner} with a highest bid of {highestBid}")



continueBidding='true'

while continueBidding:
    shouldContinue = input("There are other users who want to bid?")
    if shouldContinue=='yes'.lower():
        name = input("What's your name?")
        bidding_value = input("What's your Bid?")
        bidder_info[name]=bidding_value
    else:
        continueBidding='false'
        findHighestBidder(bidder_info)
        break

