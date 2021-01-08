from art import logo
import random

#Function to compare user's guess to the number
def compare(user_guess, number):
  """Compares user's guess to the number and will return result"""
  if user_guess > number:
    global attempts
    attempts -= 1
    return "Too high."
  elif user_guess < number:
    attempts -= 1
    return "Too low."
  else:
    return f"Congratulations! The answer was {number}."

print(logo)

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100")

#Generate a random number between 1 and 100
number = random.randrange(1, 101)

#Ask user for their desired difficulty level
level = input("Choose a dificulty level. Type 'easy' or 'hard': ")
if level == "easy":
  attempts = 10
else:
  attempts = 5

#Run the game
print(f"You have {attempts} attempts to guess the number")
while attempts !=0:
  for attempt in range(attempts):
    user_guess = int(input("Make a guess: "))
    print(compare(user_guess, number))
    if user_guess == number:
      break
    if attempts == 0 and user_guess != number:
      print (f"Sorry! The answer was {number}. You lose.")
  break