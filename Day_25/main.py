# with open("./weather_data.csv", mode='r') as weather_data :
#     data = weather_data.readlines()
#     print(data)

# import csv

# with open("./weather_data.csv", mode='r') as weather_data :
#     data = csv.reader(weather_data)
#     temperatures = []
#     count = 0
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
# 
#     print(temperatures)

import pandas
data = pandas.read_csv("./weather_data.csv")
print(type(data))
print(data)

print(type(data["temp"]))
print(data["temp"])