from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape('turtle')

colors = ['red', 'blue', 'green', 'violet', 'skyblue', 'black', 'yellow', 'salmon']


def draw_shape(no_of_sides) :
    for _ in range(no_of_sides) :
        angle = 360 / no_of_sides
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)

for num_sides in range(3,10) :
    timmy_the_turtle.color(random.choice(colors))
    draw_shape(num_sides)

screen = Screen()
screen.exitonclick()

