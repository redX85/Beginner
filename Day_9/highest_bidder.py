from art import logo
print(logo)

def find_highest_bidder(bidder_list):
    highest_bid_amount = 0
    winner = ""
    # TODO-4: Compare bids in dictionary
    for person in bidder_list:
        # define a variable that will capture the bidders bid
        current_bid_amount = bidder_list[person]
        if current_bid_amount > highest_bid_amount:
            highest_bid_amount = current_bid_amount
            winner = person
        # for the else statement nothing happens
    print(f"The winner is {winner} with a bid of ${highest_bid_amount}")

# this bids dictionary will capture things that happen in the while loop
bids = {}
continue_bidding = True

# while true
while continue_bidding:
    # TODO-1: Ask the user for input
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))

    # TODO-2: Save data into dictionary {name: price}
    # this will add to the bids dictionary outside the loop
    bids[name] = price

    # TODO-3: Whether if new bids need to be added
    continue_or_not = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    # if they dont want to continue
    if continue_or_not == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    # if they want to continue
    elif continue_or_not == "yes":
        print("\n" * 20)
    # else do nothing






