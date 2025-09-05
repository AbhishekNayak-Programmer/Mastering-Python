programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary)
print(programming_dictionary["Bug"])
print(programming_dictionary["Function"])

# Adding an Item in Dictionary
programming_dictionary["name"] = "Abhishek"
print(programming_dictionary)

# Updating a dictionary
programming_dictionary["name"] = "Abhishek Nayak"
print(programming_dictionary)

# Looping the dictionary
for key in programming_dictionary :
    print(key)
    print(programming_dictionary[key])

# Wipe/Clearing a dictionary
programming_dictionary = {}
print(programming_dictionary)


# Nesting in Dictionary
travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])

travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

print(travel_log["Germany"]["cities_visited"][2])