from turtle import Turtle, Screen, forward, screensize
import random

screen = Screen()
screen.bgcolor("#000000")
screen.setup(width=500, height=400)


is_race_on = False

colors = ["green", "blue", "pink", "red", "purple"]
y_cordinates = [-100, -50, 0, 50, 100]
all_turtles = []

user_guess = screen.textinput(
    title="Make a guess", prompt="Which turtle will win!. Make a guess using colors: "
)
pencil = Turtle() 

# Go to the corner of the screen.
pencil.penup()
pencil.speed(0)
pencil.goto(x=-250, y=200)

for i in range(24):
    pencil.pendown()
    pencil.pencolor("#ffffff")
    pencil.right(90)
    pencil.forward(500)
    pencil.left(90)
    pencil.forward(20)
    pencil.left(90)
    pencil.forward(500)
    pencil.right(90)
    pencil.forward(20)


for turtle in range(0, 5):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.goto(x=-230, y=y_cordinates[turtle])
    tim.pendown()
    tim.pencolor(colors[turtle])
    tim.color(colors[turtle])
    all_turtles.append(tim)
if user_guess:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 210:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_guess:
                print(f"You've won!👍🏼 The {winning_turtle} turtle is the winner.")
            else:
                print(f"You've loss!👎🏼 The {winning_turtle} turtle is the winner.")
        turtle.forward(random.randint(0, 50))


screen.exitonclick()
