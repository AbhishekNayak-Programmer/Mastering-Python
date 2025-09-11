from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red", 'orange', "green", "blue", "purple", "yellowgreen"]
y_position = -70
all_turtle = []

for turtle_index in range(0, 6) :
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position)
    y_position += 30
    all_turtle.append(new_turtle)

is_race_on = False

if user_bet :
    is_race_on = True

while is_race_on :
    for turtle in all_turtle :
        if turtle.xcor() > 230 :
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet :
                print("you won!")
            else :
                print(f"You lost! Turtle won is {winning_color} in color")
            
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()