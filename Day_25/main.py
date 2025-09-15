import pandas

data = pandas.read_csv("./weather_data.csv")
# print(data)
# print(type(data))

# print(data["temp"])
# print(type(data["temp"]))

# Converting data to a dictionary
data_dict = data.to_dict()
print(data_dict)
print(data_dict["temp"])
temp_list = data["temp"].to_list()
print(temp_list)

# Calculating average temprature
avg_temp = sum(temp_list) / len(temp_list)
print(avg_temp)

# Or 
average_temp = data["temp"].mean()
print(average_temp)

# Getting the maximum data from the temp
print(data["temp"].max())
# Or
print(data.temp.max())

# Getting data in column 
print(data["condition"])
print(data.condition)

# Getting Data in row
print(data[data.day == "Monday"])
max_temp_row = data[data.temp == data.temp.max()]
print(max_temp_row.condition)
print(max_temp_row.temp)


# Create a data frame from scratch
data_dict = {
    "students" : ["Adarsh", "Manas", "Abhishek"],
    "scores" : [75, 76, 99]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")