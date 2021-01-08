# ASCII art "treasure"

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

#Great the player and let's get started!
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n") 

direction = input ('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n').lower()

if direction == "left":
  action = input ("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat, type 'swim' to swim across\n").lower()
  if action == "wait":
    door = input ("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n").lower()
    if door == "blue":
      print ("You are eaten by beasts.\nGame Over!")
    elif door == "yellow":
      print ("CONGRATULATIONS!\nYOU WIN!")
    elif door == "red":
      print ("Burned by fire.\nGame Over!")
    else:
      print ("You chose a door that doesn't exist. Game Over!")
  else:
    print ("Attacked by trout.\nGame Over!")
else:
  print ("Fall into a hole.\nGame Over!")
