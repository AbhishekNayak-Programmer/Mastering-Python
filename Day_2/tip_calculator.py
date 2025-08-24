print("Welcome to the tip calculator!")
price = float(input("What was the total bill : "))
tip = int(input("How much tip % would you like to give : 10, 12 or 15 : "))
persons = int(input("How many persons are going to split the bill : "))

tip_amount = (price / 100) * tip
total_amount = (price + tip_amount) / persons

print(f"Each Person Should pay : {round(total_amount, 2)}")