# great the user when the program is run.
print("Hello there! Welcome to the tip calculator.\n")
# Ask user for information on bill total, tip amount and number of people sharing the bill.
bill = float(input ("How much is your total bill in dollars?\n"))
tip = int(input ("How much tip would you like to pay? e.g. 10, 15, 20.\n"))
people = int (input ("How many people to split the bill?\n"))
# claculate and present how much should be paid by each person.
tip_amount = bill * (tip/100)
bill_share = (bill + tip_amount)/people
final_amount = "{:.2f}".format(bill_share)
print(f"\n\nEach person should pay: {final_amount} $")
