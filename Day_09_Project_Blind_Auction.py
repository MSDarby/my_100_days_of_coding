import  auction_art
print(auction_art.logo)

bid_dict = {}

continue_bidding = True

while continue_bidding:

    name = input("What's your name: ").lower()
    bid = int(input("Whats your bid: "))

    bid_dict[name] = bid

    should_continue = input("Are there others who need to bid? type yes or no: \n").lower()

    if should_continue == 'yes':
        print("\n" * 20)
    elif should_continue == 'no':
        highest_bidder =""
        highest_bid = 0
        for key in bid_dict:
            continue_bidding = False
            print("\n" * 20)
            if bid_dict[key] >= highest_bid:
                highest_bidder = key
                highest_bid = bid_dict[key]
        print(f"the winner is {highest_bidder} with a bid of ${highest_bid}")
    else:
        print("invalid input, please restart by entering your bid again")
