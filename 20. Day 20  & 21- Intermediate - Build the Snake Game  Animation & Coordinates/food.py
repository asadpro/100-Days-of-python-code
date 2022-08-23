from turtle import Turtle
import random

# By inheriting the food class from Turtle the food class will have all the capabilities Turtle class have but in addition the food class will do
# Something more what we want it to do.


class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
