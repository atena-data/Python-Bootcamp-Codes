#import random module
import random
#ASCII arts for game choices
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print ("Welcome to Rock, Paper Scissors!\nLets Play!\n")

#Ask user for their choice
user_choice = int (input ("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))

#Generate random value as computer's choice
computer_choice = random.randint(0,2)

#List all possible choices
choices = [rock, paper, scissors]

#Check user and computer choices against each other
if user_choice >= 3 or user_choice < 0:
    print ("You typed an invalid number. Please try again!")
else:    
  print(f"You chose:\n{choices[user_choice]}")
  print(f"Computer chose:\n{choices[computer_choice]}")
  if user_choice == 0 and computer_choice == 2:
    print ("CONGRATULATIONS!\nYou won!")
  elif user_choice > computer_choice:
    print ("CONGRATULATIONS!\nYou won!")
  elif computer_choice > user_choice:
    print ("SORRY!\nYou lost!\nPlease try again.")
  elif computer_choice == user_choice:
    print ("It's a draw!")
