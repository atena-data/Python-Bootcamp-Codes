import random
from art import logo, vs
from game_data import data
from replit import clear

print(logo)

#gets the account information
def info(account):
  """Takes the account and print out information abot the account"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return name + ", a " + description + ", from " + country

#choose the first random account
a = random.choice(data)

score = 0
game_on = True

#continue the loop as long as use guesses correct answer
while game_on:
  

  #get account info for comparison
  follower_a = a["follower_count"]
  b = random.choice(data)
  #find a new account if a and b are the same account
  while b == a:
    b = random.choice(data)
  follower_b = b["follower_count"]

  #print information to user
  print(f"Compare A: {info(a)}")
  print(vs)
  print(f"Against B: {info(b)}")

  #ask user for comparison result
  user = input("Who has more followers on Instagram? Type 'A' or 'B': ").upper()
  clear()
  print(logo)
  
  #chec user answer with data
  if user == "A" and follower_a > follower_b:
    score += 1
    print (f"You're right! Current score: {score}")
  elif user == "B" and follower_b > follower_a:
    score += 1
    print (f"You're right! Current score: {score}")
  else:
    game_on = False
    print(f"Sorry you lose! Final score: {score}")
   #replace account a and b
  a = b