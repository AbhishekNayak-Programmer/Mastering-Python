# Strings 
print("Abhishek"[0]) # Reading from starting
print("Abhishek"[-1]) # Reading from ending
print("123" + "456") # This will only concatenate the strings not do any addition operation

# Integers
print(123 + 456)

# Large Numbers - These can be written in a underscore separated but will print in normal manner
print(123_456_789)

# Float
print(3.14)

# Booleans
print(True)
print(False)

# Type Checking for all data types
print(type("Abhishek"))
print(type(123))
print(type(123.3456))
print(type(True))

# Type casting
print(int(123) + int(456))
print(str(123))
print(float(123))
print(bool(1))


# Type conversion with go
print("Number of letters in your name: " + str(len(input("Enter your name : "))))


# Mathematical Operations
print(15 + 5) # Simple Addition
print(15 - 5) # Simple Substraction
print(5 * 5) # Simple Multiplication
print(5 ** 5) # Used for finding power 
print(5 / 3) # Only divides and returns the exact floating values
print(5 // 3) # Divides and trunc the decimal values


# Order of Precedence 
# PEMDAS - parenthesis, exponentiation, multiplication, division, addition, substraction
# Parenthesis () - Highest
# Exponentiation - ^
# Multiplication and Division are same priority Here order matters
# Addition and Subtraction are same priority Here order matters

print(3 * 3 + 3 / 3 - 3) # Left to right order of execution
print(3 * (3 + 3) / 3 - 3) # Left to right order of execution

# Rounding Numbers 
print(round(2.6))
print(round(2.4))

bmi = 170 / (1.2 ** 2)
print(round(bmi, 2)) # Rounding BMI upto 2 decimal points

# Short Trick for Num Manipulation
score = 1
score += 1
print(score)

# F String in python same like template literals with f and curley braces syntax
is_winning = True

print(f"Our team score is : {score} and we are going to win the match in boolean is : {is_winning}")