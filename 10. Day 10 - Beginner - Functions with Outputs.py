# Formating a name using function
# def format_name(f_name,l_name):
#     if f_name == '' or l_name == '':
#         return
#     full_name = f_name+""+l_name
#     return full_name.title()

# # If you want to print something in pascal case then we can use the title() method

# print(format_name(input('What is your f_name? '),input('What is your l_name?')))


# 👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇
# Days in Month challenge of day 10

# def is_leap(year):

# 🏆🏆🏆 Below we have  added the docstring in python which gives us a little documentation that a function do.

#   """To check whether a year is leap year or not"""
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(year, month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#   if month > 12 or month < 1 and year > 2050 or year <   1:
#       return "Both month and year are Invalid "

#   elif month > 12 or month < 1:
#       return "Invalid month"

#   elif year > 2050 or year <   1:
#       return "Invalid year"

#   if is_leap(year=year) and month == 2:

#     return 29
#   return month_days[month - 1]


# #🚨 Do NOT change any of the code below
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)


# 👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇
# Final calculator challenge of day 10

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
# 🎃🎃🎃 Below is a traditional way to solve calculator problem

# terminate = False
# resulted_value = 0
# def addition(num1, num2):
#   return f"{num1} + {num2} = {num1+num2}"

# def subtract(num1, num2):
#   return f"{num1} - {num2} = {num1-num2}"

# def multiply(num1, num2):
#   return f"{num1} * {num2} = {num1*num2}"

# def division(num1, num2):
#   return f"{num1} / {num2} = {num1/num2}"
# while not terminate:

#   first_num = int(input('What\'s the first number?: '))
#   operation = input('+\n-\n*\n/\nPick an operation: ')
#   second_num = int(input('What\'s the next number?: '))

#   if operation == "+":
#     resulted_value = addition(num1=first_num,num2=second_num)
#     print(addition(num1=first_num,num2=second_num))

#   elif operation == "-":
#     resulted_value = subtract(num1=first_num,num2=second_num)
#     print(subtract(num1=first_num,num2=second_num))

#   elif operation == "*":
#     resulted_value = multiply(num1=first_num,num2=second_num)
#     print(multiply(num1=first_num,num2=second_num))

#   elif operation == "/":
#     resulted_value = division(num1=first_num,num2=second_num)
#     print(division(num1=first_num,num2=second_num))

#   else:
#     print('Invalid operation!!!')
#     terminate=True

#   is_continue = input(f"Type 'y' to continue calculating with {resulted_value}, or type 'n' to start a new calculation: ")
#   if is_continue == "n":
#     terminate = True

# 🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍀🍀🍀🍀🍀🍀🍀🍀🍀🍀🍀🍀🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁🍁


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    print(logo)
    terminate = False
    """ Calculator is recursion function which call itself again and again and if we call it somewhere in the program it restart the whole program"""
    list_of_operations = []
    num1 = float(input("What's the first number?: "))
    while not terminate:

        for operation in operations:
            print(operation)
            list_of_operations.append(operation)
        operation = input("Pick an operation from the above line. ")
        if operation not in list_of_operations:
            terminate = True
            print("Invalid operation!!!")
            calculator()

        num2 = float(input("What's the second number?: "))

        calculation = operations[operation]
        answer = calculation(n1=num1, n2=num2)
        print(f"{num1} {operation} {num2} = {answer}")

        is_continue = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new fresh calculation? or type exit: "
        )

        if is_continue == "y":
            num1 = answer
        elif is_continue == "exit":
            terminate = True
        else:
            terminate = True
            calculator()


calculator()
