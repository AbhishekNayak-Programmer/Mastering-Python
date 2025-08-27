# import myModule
# print(myModule.my_fav_number)

import random
# random_number = random.randint(1, 10)
# print(random_number)

# random_number = random.uniform(1, 10)
# print(random_number)

# random_number = random.random() * 10

random_number = random.random()
if random_number <= 0.5:
    print("Heads")
else :
    print("Tails")


# Lists in python also known as arrays in programming
fruits = ["Cherry", "Apple", "Pear"]
print(fruits)

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
print(states_of_america[0])

states_of_america[1] = "Pencilvenia"

states_of_america.append("Abhishek Land")

states_of_america.extend(["Sahil Land", "Abhishek Nayak Land"])

print(states_of_america)
# print(states_of_america[50])
print(states_of_america[len(states_of_america) - 1])

fruits = ["Cherry", "Apple", "Pear"]
veg = ["Cucumber", "Kale", "Spinnach"]
fruits_and_veg = [fruits, veg]
print(fruits_and_veg)


# Random Bill Payment in List Example

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

print(random.choice(friends))

bill_paying_person = random.randint(0, len(friends))

print(f"Today's Bill will be paid by : {friends[bill_paying_person]}")



