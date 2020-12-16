from replit import clear
from art import logo

print(logo)

#dictionary for all the bids entered.
bids = {}
def bidders(person, bid):
  bids [person] = bid

# continue bidding as long as there are bidders
continue_bid = True
while continue_bid:
  person = input("What's your name?\n")
  bid = int(input("What's your bid?\n"))
  bid_again = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if bid_again == "yes":
    continue_bid = True
  else:
    continue_bid = False
  bidders(person, bid)
  clear()

#find highest bid  
highest = 0
winner = ""
for person in bids:
  if bids[person] > highest:
    highest = bids[person]
    winner = person

print(f"The winner is {winner} with a bid of ${highest}")