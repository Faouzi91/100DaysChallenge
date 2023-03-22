# with open("./weather_data.csv") as data:
#     datas = data.readlines()
import os

# print(datas)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data_file:
#         print(row)


import pandas

# data = pandas.read_csv(os.path.join(".", "weather_data.csv"))
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()

# # average_temp = sum(temp_list)/len(temp_list)
# # average_temp = data["temp"].mean()

# max_temp = data["temp"].max()

# # print(average_temp.__round__(2))

# # print(temp_list)
   
# # print(max_temp)

# # #get Data in columns
# # print(data["condition"])
# # print(data.condition)


# #Get a Data in Row
# # print(data[data.day == "Monday"])
# # print(data[data.temp == max_temp])
# monday = data[data.day == "Monday"]
# # print(monday.condition)

# #Celcius to Farenheit calculator

# Farenheit = (int(monday.temp) * 9/5) + 32

# print(Farenheit)



#Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# print(data)


data = pandas.read_csv(os.path.join(".", "./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"))

gray = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

data_dict = { 
    "Primary Fur Color": ["Gray", "Black", "Cinnamon"],
    "number": [gray, black, cinnamon]
} 
data = pandas.DataFrame(data_dict)
data.to_csv("file.csv")

print(data_dict)