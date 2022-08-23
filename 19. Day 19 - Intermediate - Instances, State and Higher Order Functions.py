from turtle import Turtle, Screen
import turtle
import random

screen = Screen()
# ogway = Turtle()

# def move_forward():
#     ogway.forward(10)

# def move_backward():
#     ogway.backward(10)

# def anti_clockwise():
#     ogway.left(10)

# def clockwise():
#     ogway.right(10)

# def clear():
#     screen.clear()
#     turtle.home()
#     screen.exitonclick()



# def info():
    
#     print('You have press the onkeypress button.')

# # This method will let the screen listen to what we say.
# turtle.listen()

# turtle.onkey(fun=move_forward,key='w')
# turtle.onkey(fun=move_backward,key='s')
# turtle.onkey(fun=anti_clockwise,key='a')
# turtle.onkey(fun=clockwise,key='d')
# turtle.onkey(fun=clear,key='c')

# screen.exitonclick()

# 😎😎😎😎😎😎😎😎 Turtle racing game 😎😎😎😎😎😎😎😎😎😎
# Defining colors for each turtle instance.
colors = ['red','orange','yellow','green','blue','purple']

# Defining coordinates for each of the turtle.
y_positions = [-150,-84,-18,48,114,180]

is_race_on = False
# Setting the width & height of the screen.
screen.setup(width=500,height=400)

# Creating popup box
user_bet = screen.textinput(title='Make your bet',prompt='Which turtle will win the race? Enter a color: ')
all_turtles = []
for turtle_index in range(0,6):

    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won!👍🏼 The {winning_color} turtle is the winner.")
            else:
                print(f"You've loss!👎🏼 The {winning_color} turtle is the winner.")
    
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()
