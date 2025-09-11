from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape('turtle')
timmy_the_turtle.color('greenyellow')

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]

timmy_the_turtle.pensize(15)
timmy_the_turtle.speed("fastest")

for _ in range(500) :
    timmy_the_turtle.color(random.choice(colors))
    timmy_the_turtle.forward(30)
    timmy_the_turtle.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()

