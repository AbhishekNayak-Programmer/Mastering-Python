from turtle import Turtle, Screen, colormode
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape('turtle')
timmy_the_turtle.color('greenyellow')

# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]

timmy_the_turtle.pensize(15)
timmy_the_turtle.speed("fastest")
colormode(255)

def random_color_generator():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color

for _ in range(500) :
    timmy_the_turtle.color(random_color_generator())
    timmy_the_turtle.forward(30)
    timmy_the_turtle.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()

