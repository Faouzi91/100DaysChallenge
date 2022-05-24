# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}

# #TODO-2: Write your code below to add the grades to student_grades.👇
# for key in student_scores:
#     score = student_scores[key]
#     if score > 90:
#         student_grades[key] = "Outstanding"
#     elif score > 80:
#         student_grades[key] = "Exceeds Expectations"
#     elif score > 70:
#         student_grades[key] = "Acceptable"
#     else:
#         student_grades[key] = "Fail"


# # 🚨 Don't change the code below 👇
# print(student_grades)






# TODO All about dictionaries

# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }

# #TODO:Retrieving items from dictionary
# print(programming_dictionary["Loop"])

# #TODO: Adding new items to dictionary.
# programming_dictionary["Loop"] = "The action of doing something over and over again"

# #TODO create an empty dictionary
# empty_dictionary = {}

# #TODO Wipe an existiong dictionary.
# # programming_dictionary = {}
# # print(programming_dictionary)


# #TODO Edit an item in a dictionary.
# programming_dictionary["Bug"] = "A moth in your computer"

# #TODO Loop throught a dictionary
# for key in programming_dictionary:
#   print(key)
#   print(programming_dictionary[key])

# #TODO Nesting
# capitals = {
#     "Cameroon": "Yaounde",
#     "France": "Paris",
# }

# #TODO nesting a list in a dictionary

# travel_log = {
#     "Cameroun": ["Ngaoundere", "Banyo", "Maroua", "Garoua"],
# }


# #TODO Nesting a dictionary in a dictionary
# travel_log = {
#     "Cameroun": {
#         "cities_visited": ["Ngaoundere", "Banyo", "Maroua", "Garoua"],
#         "total_visits": 12
#     }
# }

# #TODO Nesting a dictionary in a list
# travel_log = [
#     {
#         "Country": "Cameroun",
#         "cities_visited": ["Ngaoundere", "Banyo", "Maroua", "Garoua"],
#         "total_visits": 12
#     },
#     {
#         "Country": "Germany",
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 5
#     },
# ]





# # TODO Challenge about dictionaries

# travel_log = [
#     {
#         "country": "France",
#         "visits": 12,
#         "cities": ["Paris", "Lille", "Dijon"]
#     },
#     {
#         "country": "Germany",
#         "visits": 5,
#         "cities": ["Berlin", "Hamburg", "Stuttgart"]
#     },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇


# def add_new_country(country, visits, cities):
#     empty_list = {}
#     empty_list["country"] = country
#     empty_list["visits"] = visits
#     empty_list["cities"] = cities
#     travel_log.append(empty_list)


# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)


from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)


def aunction():
  other_bidders = True
  bidders = {}

  amount = []
  while other_bidders:
    name = input("Waht is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid
    other = input(
        'Are there other bidders? Type "yes" to confirm otherwise type "no": ')
    clear()
    if other == "no":
      other_bidders = False

    print(bidders)
  for person in bidders:
    amount.append(bidders[person])
  print(max(amount))


aunction()
