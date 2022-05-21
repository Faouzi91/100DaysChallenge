import random


# number = random.randint(0,1)
# number2 = random.random()
# number3 = random.randrange(0,10)
# number4 = random.uniform(0,10)

# print(number)
# print(number2)
# print(number3)
# print(number4)

# a_list =  input("Enter a list of numbers: ")
# print(a_list.split(","))
# a_list = a_list.split(",")
# print(len(a_list))

# # 🚨 Don't change the code below 👇
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)

# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# length = len(names)
# index = random.randint(0, length - 1)

# name = names[index]

# print(f"{name} is going to buy the meal today!")


# # 🚨 Don't change the code below 👇
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇


# column = int(position[0])
# row = int(position[1])

# # selected_row = map[row - 1]
# # selected_row[column - 1] = "X"

# map[row -1][column -1] = "X"

# #print(treasure_room)


# #Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")


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

#Write your code below this line 👇

user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.  "))

choices = [rock, paper, scissors]
length = len(choices) - 1
cpu_choice = random.randint(0, length)


if user_choice == 0 and cpu_choice == 1:
  print("You lost!\n")
  print("You chose: \n", choices[user_choice])
  print("The Computer chose\n:", choices[cpu_choice])
elif user_choice == 0 and cpu_choice == 2:
  print("You win!\n")
  print("You chose: \n", choices[user_choice])
  print("The Computer chose\n:", choices[cpu_choice])
elif user_choice == 1 and cpu_choice == 0:
  print("You win!\n")
  print("You chose: \n", choices[user_choice])
  print("The Computer chose\n:", choices[cpu_choice])
elif user_choice == 1 and cpu_choice == 2:
  print("You lose!\n")
  print("You chose: \n", choices[user_choice])
  print("The Computer chose\n:", choices[cpu_choice])
elif user_choice == 2 and cpu_choice == 0:
  print("You lose!\n")
  print("You chose: \n", choices[user_choice])
  print("The Computer chose\n:", choices[cpu_choice])
elif user_choice == 2 and cpu_choice == 1:
  print("You win!\n")
  print("You chose: \n", choices[user_choice])
  print("The Computer chose\n:", choices[cpu_choice])
elif user_choice == cpu_choice:
  print("Its a draw!\n")
  print("You chose: \n", choices[user_choice])
  print("The Computer chose\n:", choices[cpu_choice])
else:
  print("You typed an invalid number. You lose.")
