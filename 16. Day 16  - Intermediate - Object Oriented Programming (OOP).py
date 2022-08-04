# import turtle
# t = turtle.Turtle()
# # t.shape('turtle')
# # t.right(90)
# # t.forward(100)
# # t.left(90)
# # t.backward(100)
# # t.forward(100)
# # t.goto(100,150)
# # t.home()
# t.shape('turtle')
# t.color('red','green')


# def rectangle():
#     """This turtle will create a rectangle shape"""
#     i =0 
#     while i !=3:
#             i+=1
#             t.forward(250)
#             t.right(90)
#             t.forward(100)
#             t.right(90)
#             t.forward(250)
#             t.right(90)
#             t.forward(100)
#             t.home()

# def square():

#     t.forward(100)
#     t.right(90)
#     t.forward(100)
#     t.right(90)
#     t.forward(100)
#     t.right(90)
#     t.forward(100)
#     t.home()

# def triangle():
#     """Creating a triangle"""
#     t.right(90)
#     t.forward(100)
#     t.right(90)
#     t.forward(100)
#     t.right(40)
#     t.home()


# def equalateral():
#     """Creating equalateral shape of geomatery"""
#     while True:
#         t.right(45)
#         t.forward(150)
#         t.right(135)
#         t.forward(200)
#         t.right(135)
#         t.home()


# def circle():
#     """Creating a cricle manually"""
#     for i in range(27):
#         t.right(i)
#         t.forward(i)


# def create_plus():
#     for i in range(3):
#         t.forward(100)
#         t.stamp()
#         if i == 2:
#             for i in range(6):
#                 t.backward(100)
#                 t.stamp()
#                 if i == 5:
#                     t.home()
#                     t.left(90)
#                     for i in range(3):
#                         t.forward(100)
#                         t.stamp()
#                         if i == 2:
#                             t.home()
#                             t.right(90)
#                             for i in range(3):
#                                 t.forward(100)
#                                 t.stamp()
#                                 if i == 2:
#                                     t.home()


# equalateral()
# # triangle()
# # Create a plus symbol with stamps
# # create_plus()    

# # Creating circle in descending order
# # def des_circle():
# #     for i in range(11):
# #         t.circle(100)
# #         t.right(35)

# # Creating circle in ascending order
# # def asc_circle():
# #     for i in reversed(range(10,110,10)):
# #         t.circle(i)

# # des_circle()
# # asc_circle()

# # for i in reversed(range(10,100,10)):
# #     print(i)

# # t.fillcolor('purple')
# # t.begin_fill()
# # circle()
# # t.end_fill()

# # t.fillcolor('Green')
# # t.speed(10)
# # t.begin_fill()
# # square()
# # t.end_fill()


# # t.shapesize(3.0,4.0,2.0)
# # t.pensize(12)
# # t.pencolor('purple')
# # t.circle(radius=100)

# # t.dot(100)
# # turtle.bgcolor('black')
# # turtle.title('My Turtle program')


# # Cloning a turtle


# t1 = t.clone()

# t1.speed(5)

# t1.pen(pencolor='purple',pensize=4, fillcolor='yellow' )

# colors = ['blue','green','yellow','cyan','brown','red','purple','pink']

# def string():
#     j =0 
#     for i in range(20):    
#         for color in range(len(colors)):
#             t1.pencolor(colors[color])
#             t1.right(90)
#             t1.circle(50)

#             t1.left(90)
#             t1.circle(50)

#             t1.left(90) 
#             t1.circle(50)

#             t1.left(90)
#             t1.circle(50)


# screen = turtle.Screen()
# screen.canvheight
# screen.canvwidth
# # Screen will be exit only when we click on it.
# # screen.exitonclick()

# string()

# 🍟🍟🍟🍟🍟 Pretty table package and their usage with detail 🍟🍟🍟🍟🍟

# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'], align='l')
# table.add_column('Type', ['Electric', 'Water', 'Fire'], align="l")
#
# print(table)
#
# # 🍀🍀🍀🍀Importing data from CSC File in pretty table package🍀🍀🍀🍀
# import prettytable
# with open("prettyTable.csv") as pt:
#     excel_table = prettytable.from_csv(pt)
#
# # Right align the column in a table
# excel_table.align['Name'] = 'r'
# # Center align the column in a table
# excel_table.align['Test Score 1'] = 'l'
# print(excel_table)
#
# # Print only 4 rows and two columns in a table
# print(excel_table.get_string(start=1, end=4, fields=['Name', 'Test Score 1']))

# 🍀🍀🍀🍀🍀 OOP Version of Coffee machine  🍟🍟🍟🍟🍟
