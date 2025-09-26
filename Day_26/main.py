# List Comprehension
numbers = [1,2,3]
new_lists = [n + 1 for n in numbers]
print(new_lists)

# List Comprehension
name = "Abhishek"
letter_list = [letter for letter in name]
print(letter_list)

# List Comprehension along with range
range_list = [num * 2 for num in range(2, 10)]
print(range_list)

# List Comprehension along with conditions
names = ["Abhishek", "Sahil", "Adarsh", "Little", "Sradhanjali", "Surendra", "Kshitun"]
short_names = [name for name in names if len(name) < 7]
print(short_names)

uppercase_long_names = [name.upper() for name in names if len(name) >= 7]
print(uppercase_long_names)

import random

ages = {people:random.randint(1, 100) for people in names}
print(ages)

old_age = {people_name:age for (people_name, age) in ages.items() if age >= 60}
print(old_age)