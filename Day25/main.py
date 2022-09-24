# with open("./weather_data.csv") as data:
#     datas = data.readlines()

# print(datas)

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    for row in data_file:
        print(row)