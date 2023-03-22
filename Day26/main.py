import random
# #List Comprehension
# numbers = [1, 2, 3, 4, 5, 6, 7]
# # new_list = []
# # for n in numbers:
# #     add_1 = n + 1
# #     new_list.append(add_1)
# #     print(new_list)
    
# # new_list = [new_item for item in list]
# new_list = [n + 1 for n in numbers]
# print(new_list)

# name = "Khadija"
# new_list = [letter for letter in name]
# print(new_list)

# list = range(1,5)

# new_list = [number*2 for number in list]
# print(new_list)


#Conditional list comprehension
# new_list = [new_item for item in list if test]

# names = ["Alex", "Fawzanne", "Aboubakar", "Oumar", "Uthman", "Aliou", "Putin"]
# # short_names = [name.upper() for name in names if len(name) < 6]
# # print(short_names)


# # numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # # squared_numbers = [number * number for number in numbers]
# # # print(squared_numbers)


# # results = [number for number in numbers if number%2 == 0]
# # print(results)






# # Dictionary Comprehension new_dict = {new_key: new_value for item in dictionary}

# # creating a new dictionary based on the value of an existing dictionary new_dict = {new_key: new_value for (item, value) in dictionary.items() if test}

# students_scores = {student:random.randint(1, 100) for student in names}
# print(students_scores)

# passed_students = { student: score for (student, score) in students_scores.items() if score >= 50}
# print(passed_students)


# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆

# # Write your code below:
# result = {word: len(word) for word in sentence.split()}


# print(result)


# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆 

# weather_f = {day: (temp_c * 9/5) + 32
#              for (day, temp_c) in weather_c.items()}
# # Write your code 👇 below:


# print(weather_f)

import pandas

student_dict = {
    "student": ["Angela", "Aboubakar", "James", "Lily"],
    "score": [56, 76, 98, 100],
}
 
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through a dataframe 


# loop through each of the rows of the dataframe
for (index, row) in student_data_frame.iterrows():
    print(row)
