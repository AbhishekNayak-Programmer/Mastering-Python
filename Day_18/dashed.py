from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape('turtle')
timmy_the_turtle.color('yellowgreen')


for _  in range(1, 15) :
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()

screen = Screen()
screen.exitonclick()

