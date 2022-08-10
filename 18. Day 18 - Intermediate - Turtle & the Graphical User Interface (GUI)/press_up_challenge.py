import random
from turtle import Screen, Turtle
import turtle as t
t.colormode(255.0)

tr = Turtle()
tr.pensize(4)
# tr.shapesize(2)
tr.speed(0)

# colors = ['brown','green','black','red','purple','pink','violet','yellow','blue']

# 🌎🌎🌎🌎 Random walk challenge 🌎🌎🌎🌎

# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     rgb = (r,g,b)
#     return rgb


# directions = [0,90,180,270]
# for _ in range(100):
#     tr.forward(50)
#     tr.pencolor(random_color())
#     tr.color(random_color())
#     tr.setheading(random.choice(directions))

# 🌎🌎🌎🌎 Make a Spirograph challenge 🌎🌎🌎🌎

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r,g,b)
    return rgb

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tr.pencolor(random_color())
        tr.circle(150)
        tr.setheading(tr.heading() + size_of_gap)


draw_spirograph(10)
screen = Screen()
screen.exitonclick()

