import os
logo = '''
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
bids={}

bidding_finished=False

def find_highest_bidder(bidding_record):
        for bidder in bidding_record:
                bid_amount= bidding_record[bidder]
                highest_bid=0
                if bid_amount> highest_bid:
                        highest_bid= bid_amount
                        winner= bidder
        print(f"THe winner is {winner} with a bid of ${highest_bid}")                

while not bidding_finished: 
        name= input("What is your name?: ")
        price=int(input("What is your bid?: $"))

        bids[name]= price
        should_continue= input("Are there any other bidders? Type 'Yes' or 'No'.").lower()
        if should_continue == "no":
                bidding_finished=True
                find_highest_bidder(bids)
        elif should_continue== "yes":
                os.system('cls' if os.name=='nt' else 'clear')          