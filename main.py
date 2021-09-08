from art import logo

print(logo)
print("Welcome to the secret auction program.")

bidders = {}

def bidding():
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    next = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    bidders[name] = bid

    print('\n'*80)

    if next == "yes":
        bidding()
    elif next == "no":
        winning_bid = 0
        winning_name = ""
        for bidder in bidders:
            if bidders[bidder] > winning_bid:
                winning_name = bidder
                winning_bid = bidders[bidder]

        print(f"The winner is: {winning_name} with a bid {winning_bid}.")

    else:
        next = input("Are there any other bidders? Type 'yes' or 'no'.\n")
        bidding()

bidding()
