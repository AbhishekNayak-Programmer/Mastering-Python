# For Loops
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits :
    print(fruit)
    print(fruit + " Pie")

# For loops in practice
from asyncio.windows_events import INFINITE

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
total_score = sum(student_scores)
print(total_score)
print(max(student_scores))
print(min(student_scores))

# Finding the max and min
max_score = 0
min_score = INFINITE
for score in student_scores :
    if max_score < score :
        max_score = score
    if min_score > score :
        min_score = score

print(max_score, min_score)

# More about loops in python
for num in range(1, 10 + 1, 2) : # (start, end + 1, increments/jumps)
    print(num)

for num in range(10, 0, -2) : # (start, end - 1, decrements/jumps)
    print(num)

total = 0
for num in range(1, 101) :
    total += num
print(total)


import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Way of Generating Password
# password = ""
#
# for char in range(1, nr_letters + 1) :
#     randInd = random.randint(0, len(letters))
#     password += letters[randInd]
#
# for char in range(1, nr_symbols + 1) :
#     randInd = random.randint(0, len(symbols))
#     password += symbols[randInd]
#
# for char in range(1, nr_numbers + 1) :
#     randInd = random.randint(0, len(numbers))
#     password += numbers[randInd]
#
# print(password)

# Hard Way of Generating
password_list = []

for char in range(1, nr_letters + 1) :
    randInd = random.randint(0, len(letters))
    password_list += letters[randInd]

for char in range(1, nr_symbols + 1) :
    randInd = random.randint(0, len(symbols))
    password_list += symbols[randInd]

for char in range(1, nr_numbers + 1) :
    randInd = random.randint(0, len(numbers))
    password_list += numbers[randInd]

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""

for char in password_list :
    password += char

print(password)