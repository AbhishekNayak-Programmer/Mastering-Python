from turtle import Screen, Turtle
import pandas

screen = Screen()
turtle = Turtle()

screen.title("U.S States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("./50_states.csv")

correct = 0
guessed_states = []

while correct <= 50 :
    answer_state = screen.textinput(title=f"{correct}/{50} State Correct", prompt="What's another state's name").title()
    if answer_state == 'Exit':
        break
    if answer_state in data["state"].values:
        correct += 1
        guessed_states.append(answer_state)
        # Update the coordinate with current answer
        state_data = data[data.state == answer_state]
        new_turtle = Turtle()
        new_turtle.penup()
        new_turtle.hideturtle()
        new_turtle.goto(state_data.x.item(),state_data.y.item())
        new_turtle.write(answer_state)


# Printing the missing states
states = data.state.to_list()
missingStates = []
for state in states:
    if state not in guessed_states:
        missingStates.append(state)

data_dict = {
    "states" : missingStates
}

data = pandas.DataFrame(data_dict)
data.to_csv("states_to_learn.csv")