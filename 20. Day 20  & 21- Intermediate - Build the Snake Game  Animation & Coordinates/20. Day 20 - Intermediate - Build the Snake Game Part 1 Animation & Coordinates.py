from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")

# Tracer method turn off the animation on the screen until the update method called.
screen.tracer(0)

# 🧨🧨🧨🧨🧨🧨🧨 This code is dead because we separate it into a different class name snake

# # Snake body longivity track record.
# starting_positions = [(0, 0), (-20, 0), (-40, 0)]
# segment = []

# # Create the snake body
# for position in starting_positions:
#     new_segment = Turtle(shape="square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segment.append(new_segment)


game_is_on = True

# Creating snake object from Snake class.
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()


screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

counter = 0
while game_is_on:
    screen.update()  # Update method will update the screen pixel by pixel like a full animation picture shown on screen smoothly.
    time.sleep(0.1)

    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        snake.extend()
        food.refresh()

    # Detect collision with wall.
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail.

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()








# 🧨🧨🧨🧨🧨🧨🧨 This code is dead because we separate it into a different class name snake
# for seg_name in range(len(segment)-1,0,-1): # This line of code will take the position of every chunk of the snake

#     x_cord= segment[seg_name - 1].xcor()
#     y_cord= segment[seg_name - 1].ycor()

#     segment[seg_name].goto(x=x_cord,y=y_cord) # Here seg_name will pick snake segment and will push it to the place of onward segment in parallel with it.

# segment[0].forward(20) # We will move forward only the first chunk of the snake


screen.exitonclick()
