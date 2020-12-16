from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#takes the text and shift the letters.
def caesar(start_text, shift_number, direction):
  new_text = ''
  for letter in text:
    if letter in alphabet:
      position = alphabet.index(letter)
      if direction == "encode":
        new_position = position + shift
        if new_position <= 25:
          new_letter = alphabet[new_position]
        else:
          new_letter = alphab[new_position-26]
      elif direction == "decode":
        new_position = position - shift
        new_letter = alphabet[new_position]
      new_text += new_letter
    else:
      new_text += letter
  print(f"The {direction}d text is {new_text}")

#check if user wants to continue the game.
game_on = True
while game_on:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))


  caesar(start_text=text, shift_number=shift, direction=direction)
  play_again = input("Would you like to play agian? Type 'yes' or 'no'\n")
  if play_again == "no":
    game_on = False