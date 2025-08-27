import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user = int(input("Type 1 for Rock, 2 for Paper and 3 for Scissor : "))

if user == 1:
    print(rock)
elif user == 2:
    print(paper)
elif user == 3:
    print(scissors)

computer = random.randint(1,3)
print("Computer Choose")

if computer == 1:
    print(rock)
elif computer == 2:
    print(paper)
elif computer == 3:
    print(scissors)



if user == 1 and computer == 1 or user == 2 and computer == 2 or user == 3 and computer == 3 :
    print("It's a Draw!")
elif computer == 1 and user == 3 or computer == 2 and user == 1 or computer == 3 and user == 2:
    print("Computer Wins!")
elif user == 1 and computer == 3 or user == 2 and computer == 1 or user == 3 and computer == 2 :
    print("User Wins!")
else :
    print("Invalid Entry by User")