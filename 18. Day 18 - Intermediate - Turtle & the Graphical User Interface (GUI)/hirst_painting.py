import random

from turtle import Screen, Turtle, goto
import turtle as t
import colorgram

t.colormode(255.0)

tr = Turtle()
tr.pensize(2)


# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     rgb = (r, g, b)
#     return rgb


# 🏰🏰🏰🏰🏰 Making eight shape 🏰🏰🏰🏰🏰

# for j in range(101):
#     tr.pencolor(random_color())
#     tr.right(180)
#     tr.circle(j+10)


# 🏰🏰🏰🏰🏰 Extracting color from image using colorgram package. 🏰🏰🏰🏰🏰

# rgb_colors = []
# colors = colorgram.extract("image.jpg", 20)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.r
#     b = color.rgb.r
#     rgb = (r,g,b)
#     rgb_colors.append(rgb)

# print(rgb_colors)

color_list = [
    (254, 254, 254),
    (101, 101, 101),
    (100, 100, 100),
    (207, 207, 207),
    (213, 213, 213),
    (56, 56, 56),
    (49, 49, 49),
    (187, 187, 187),
    (25, 25, 25),
    (217, 217, 217),
    (239, 239, 239),
    (189, 189, 189),
    (124, 124, 124),
    (160, 160, 160),
    (89, 89, 89),
    (237, 237, 237),
    (242, 242, 242),
    (51, 51, 51),
    (46, 46, 46),
    (64, 64, 64),
]

import random

tr.speed(0)
tr.penup()

# Hiding the turtle
tr.hideturtle()

tr.setheading(225)
tr.forward(300)
tr.setheading(0)


for dot_count in range(1, 101):
    tr.dot(20, random.choice(color_list))
    tr.forward(50)

    if dot_count % 10 == 0:
        tr.setheading(90)
        tr.forward(50)
        tr.setheading(180)
        tr.forward(500)
        tr.setheading(0)

screen = Screen()
screen.exitonclick()
