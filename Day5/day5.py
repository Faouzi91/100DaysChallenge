import random
# fruits = ["Apple", "Pear", "Banana"]

# for item in fruits:
#     print(item)

# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆


# #Write your code below this row 👇

# print(student_heights)

# height = 0
# number_of_heights = 0
# for item in student_heights:
#     height += item
#     number_of_heights += 1

# avg_height = round(height/number_of_heights)

# print(avg_height)


# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# maximum = 0
# for score in student_scores:
#     if maximum < score:
#         maximum = score
#     else:
#         maximum = maximum

# print(f"The highest score in the class is: {maximum}")


# #Write your code below this row 👇

# result = 0
# for number in range(0, 101, 2):
#     result += number

# print(result)

# #Write your code below this row 👇

# for num in range(1, 101):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)
        
        
#Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
    'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# #Eazy Level - Order not randomised:
# #e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# len_lett = len(letters)
# len_num = len(numbers)
# len_symb = len(symbols)

# index = 0
# lett = ""

# index2 = 0
# num = ""

# index3 = 0
# symb = ""

# password = ""
# indx = 0

# for letter in range(0, nr_letters):
#   index = random.randint(0, len_lett-1)
#   lett += letters[index]

# for number in range(0, nr_numbers):
#   index2 = random.randint(0, len_num - 1)
#   num += numbers[index2]

# for symbol in range(0, nr_symbols):
#   index3 = random.randint(0, len_symb - 1)
#   symb += symbols[index3]

# combine = lett + num + symb


# #Hard Level - Order of characters randomised:
# #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


# combine = list(combine)

# random.shuffle(combine)

# print(combine)

# for item in combine:
#   password += item


# print("Your password is: " + password)


###### Her solution ######

# password = ""
# random_char = ""

# for char in range(0, nr_letters):
#     password += random.choice(letters)
    

# for char in range(0, nr_numbers):
#     password += random.choice(numbers)


# for char in range(0, nr_symbols):
#     password += random.choice(symbols)

# print(password)


password_list = []
password = ""

for char in range(0, nr_letters):
    password_list += random.choice(letters)
    

for char in range(0, nr_numbers):
    password_list += random.choice(numbers)


for char in range(0, nr_symbols):
    password_list += random.choice(symbols)


random.shuffle(password_list)

for char in password_list:
    password += char

print("Your password is: " + password)