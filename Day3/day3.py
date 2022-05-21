# print("Welcome to the rollercoaster!")
# print("-----------------------------")
# print("                             ")
# height = int(input("What is your height in cm? "))
# age = int(input("How old are you? "))
# photos = int(input("Do you want some photos? \nType 1 for Yes\nType 2 for No \n"))

# if height >= 120:
#     print("You can ride the rollercoaster")
#     if age >= 18:
#         if photos == 1:
#             print("You have to pay $15.")
#         else:
#             print("You have to pay $12.")
#     elif (age >= 12):
#         if photos == 1:
#             print("You have to pay $10.")
#         else:
#             print("You have to pay $7.") 
#     else:
#         if photos == 1:
#             print("Pay $8 please.")
#         else:
#             print("Pay $5 please.")
# else:
#     print("Sorry you have to grow taller before you can ride.")



# print("Welcome to the rollercoaster!")
# print("-----------------------------")
# print("                             ")
# height = int(input("What is your height in cm? "))
# age = int(input("How old are you? "))
# bill = 0

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     if age < 12:
#         bill = 5
#         print(f"Child tickets are ${bill}.")
#     elif age <= 18:
#         bill = 7
#         print(f"Youth tickets are ${bill}.") 
#     elif age >= 45 and age <=55:
#         print(f"Everythong is going to be ok. Have a free ride on us!")
#     else:
#         bill = 12
#         print(f"Adult tickets are ${bill}.")
        
#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         #Add $3 to the bill
#         bill += 3
#     print(f"Your final bill is ${bill}")
        
    
# else:
#     print("Sorry you have to grow taller before you can ride.")





# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# bill = 0
# if size == "S":
#     bill = 15
# elif size == "M":
#     bill = 20
# else:
#     bill = 25
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is: ${bill}.")


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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
choice1 = input(
    'You\'re at a crossroad. Where do you want to go? Type "left" or "right"  \n\n').lower()

if choice1 == "right":
  print("You fell into a hole. Game Over.")
elif choice1 == "left":
  choice2 = input(
      'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n\n').lower()
  if choice2 == "swim":
    print("You get attacked by an angry trout. Game Over.")
  elif choice2 == "wait":
    choice3 = input(
        "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?  \n\n").lower()
    if choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    elif choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    else:
      print("You chose a door that doesn't exist. Game Over.")
