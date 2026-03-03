import os

import art

print(art.logo)



bidder_dict= {}

def find_highest_bidder(bidder_dictionary):
    maxBid = bidder_dict[bidderName]
    bidder=None
    for key in bidder_dictionary:
        if bidder_dictionary[key] > maxBid:
            maxBid=bidder_dictionary[key]
            bidder = key
    print("\n" * 20)
    print(f"{bidder} is the highest bidder")


should_continue='true'
while should_continue:
    bidderName = input("Enter the name of the bidder: ")
    bidPrize = input("Enter the prize of the bidder: ")
    bidder_dict[bidderName] = bidPrize
    another_bidder=input("If there are other users who want to bid?")
    if another_bidder=='yes':
        print("\n" * 20)
        newBidderName = input("Enter the name of the bidder: ")
        newBidPrize = input("Enter the prize of the bidder: ")
        bidder_dict[newBidderName] = newBidPrize
    else:
        if len(bidder_dict) == 1:
            print(f"{bidderName} is the highest bidder")
        else:
            find_highest_bidder(bidder_dict)
        break

