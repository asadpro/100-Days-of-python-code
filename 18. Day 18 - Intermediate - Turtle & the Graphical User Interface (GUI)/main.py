from random import random
from re import L
from secrets import choice
from turtle import Screen, Turtle 

# 🚩🚩🚩🚩 Challenge of creating square using turtle 🚩🚩🚩🚩
tr = Turtle()
tr.color('red')
tr.pensize(width=2)
tr.shapesize(2)

# We can create a square using function  
# def square():
#     tr.right(90)
#     tr.forward(200)

# square()
# square()
# square()
# square()

# # We can also create square using for loop
# for i in range(4):
#     tr.right(90)
#     tr.forward(200)


# 🚩🚩🚩🚩 Challenge of creating dashed square using turtle 🚩🚩🚩🚩

# def single_line():
#     """Creating a single dotted line of 10 paces"""
#     for i in range(10):
#         tr.forward(10)
#         tr.penup()
#         tr.forward(10)
#         tr.pendown()
# def dotted_square():
#     """Making the full version of dotted square."""
#     for i in range(4):
#         single_line()
#         tr.right(90)


# dotted_square()

# 🧭🧭🧭🧭🧭 Draw a triangle, Square, pentagon, hexagon, heptagon, octagon, nonagon and decagon 🧭🧭🧭🧭🧭

# import random

# def triangle():
#     """Making triangle"""
#     for _ in range(3):
#         tr.rt(120)
#         tr.fd(100)


# def square():
#     """Creating square"""
#     for _ in range(4):
#         tr.rt(90)
#         tr.fd(100)

# def pentagon():
#     """Creating pentagon"""
#     for _ in range(5):
#         tr.rt(72)
#         tr.fd(100)

# def hexagon():
#     """Creating hexagon"""
#     for _ in range(6):
#         tr.rt(60)
#         tr.fd(100)

# def heptagon():
#     """Creating heptagon"""
#     for _ in range(7):
#         tr.rt(60)
#         tr.fd(100)

# def octagon():
#     """Creating octagon"""
#     for _ in range(8):
#         tr.rt(45)
#         tr.fd(100)

# def nonagon():
#     """Creating nonagon"""
#     for _ in range(9):
#         tr.rt(40)
#         tr.fd(100)

# def decagon():
#     """Creating decagon"""
#     for _ in range(10):
#         tr.rt(36)
#         tr.fd(100)


# all_shapes = [triangle(),square(),pentagon(),hexagon(),octagon(),nonagon(),decagon()]


# for shape in all_shapes:
#     shape

# 🌅🌅🌅🌅 We can achieve the above with the following also

def draw_shape(num_side,pcolor):
    for _ in range(num_side):
        tr.pencolor(pcolor)
        tr.rt(360/num_side)
        tr.fd(100)

for shape_side in range(3,10):
    colors = ['brown','green','black','red','purple','pink','violet','yellow','blue']
    draw_shape(shape_side,pcolor=choice(colors))


screen = Screen()
screen.exitonclick()