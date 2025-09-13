# with open("text.txt") as file:
#     contents = file.read()
#     print(contents)

with open("new_file.txt", mode='w') as file:
    file.write("\nAbhishek Nayak")

with open("text.txt", mode='a') as file:
    file.write("\nAbhishek Nayak")