from art import logo
from replit import clear
import random

def deal_card():
  """Draws a random card from the card deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def score_count(cards):
  """Takes a list of cards and returns the total score"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  elif 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
    return sum(cards)
  else:
    return sum(cards)

def compare(player_score, computer_score):
  """Compares user and computer scores"""
  if player_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"

  if computer_score == player_score:
    return "It's a draw! 🙃"
  elif computer_score == 0:
    return "You lose! The opponent has BlackJack.  😱"
  elif player_score == 0:
    return "You win with a BlackJack! 😎"
  elif player_score > 21:
    return "You went over, you lose! 😭"
  elif computer_score > 21:
    return "Oponent went over 21. You win 😁"
  elif player_score > computer_score:
    return "You win! 😃"
  else:
    return "You lose! 😤"

#Recursive function to play again
def play_game():
  print(logo)
  game_on = True
  #Draw cards for the user and the computer
  computer_card = []
  player_card = []
  for i in range(2):
    computer_card.append(deal_card())
    player_card.append(deal_card())

  while game_on:
    #calculate total score for the user and the computer
    computer_score =  score_count(computer_card)
    player_score = score_count(player_card)
    #show results to the user
    print(f"   Your cards: {player_card}, current score: {player_score}")
    print(f"   Computer's first card: {computer_card[0]}")

    if computer_score == 0 or player_score == 0 or player_score >21:
      game_on = False
    else:
      new_card = input("type 'y' to draw another card, type 'n' to pass: ")
      if new_card == "y":
        player_card.append(deal_card())
      else:
        game_on = False

  while computer_score != 0 and computer_score < 17:
    computer_card.append(deal_card())
    computer_score =  score_count(computer_card)

  #Reveal the results
  print(f"   Your final hand: {player_card}, final score: {player_score}")
  print(f"   Computer's final hand: {computer_card}, final score: {computer_score}")

  #compare results after drawing new cards
  print(compare(player_score, computer_score))

  #Ask user if they want to play
  
while input(" Would you like to play a game of BlackJack? type 'y' or 'n': ") == "y":
  clear()
  play_game()