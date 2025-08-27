# IF ELSE Condition
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry you have to grow taller before you can ride.")

# Checking a prime number 
num = int(input("Please enter a number : "))
if num % 2 == 0 :
    print("Even Number")
else :
    print("Odd Number")

# Nested IF else Statement and else if conditions
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("Enter you age "))
    if age > 18 :
        print("you have to pay $12")
    elif age >= 12 and age <= 18 :
        print("you have to pay $7")
    else:
        print("you have to pay $5")
else:
    print("Sorry you have to grow taller before you can ride.")


# BMI Calculator
weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi < 18.5 :
    print("underweight")
elif bmi >= 18.5 and bmi <= 25 : 
    print("normal weight")
else :
    print("overweight")


# Rollercoaster bigger example
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    amount = 0

    if age <= 12:
        amount = 5
        print("Please pay $5.")
    elif age <= 18:
        amount = 7
        print("Please pay $7.")
    else:
        amount = 12
        print("Please pay $12.")

    photos_needed = input("Did you want photos/videos - Please Write Yes or No : ")
    if photos_needed == "Yes" :
        amount += 3

    print(f"The total amount which you will pay is : {amount}")
else:
    print("Sorry you have to grow taller before you can ride.")

# Pizza Delivery Program
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

amount = 0

if size == "S" :
    amount += 15
elif size == "M" :
    amount += 20
else :
    amount += 25

if pepperoni == 'Y':
    if size == "S" :
        amount += 2
    else :
        amount += 3

if extra_cheese == "Y" :
    amount += 1

print(f"Your final bill is ${amount}")

# Logical Operators
