logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
def highest_bidder(bidding_dictionary):
    winner = ""
    total_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > total_bid:
            total_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${total_bid}")

bid = {}
uncomplete = True
while uncomplete:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bid[name] = price
    should_continue = input("Would you like to continue (y/n)? ").lower()
    if should_continue == "y":
        print("\n" * 20)
    if should_continue == "n":
        uncomplete = False
        highest_bidder(bid)