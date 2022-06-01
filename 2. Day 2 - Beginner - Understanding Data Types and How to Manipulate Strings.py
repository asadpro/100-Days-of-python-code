""" In Day 2 we will learn about 
Data types, Numbers, Operations, Type conversion, f-Strings
"""

from calendar import month
from cgitb import reset


# print('asad'[-1])
# print(123456789)

# str(varname) with str function we can convert any type of value into string
# type(varname) with type ftn we can check the type of variable
# float(varname) with float we can convert integer value to float

# 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# Below line will first convert string into integer then it will add it.
# sum = int(two_digit_number[0])+int(two_digit_number[1])
# print(sum)

# PEMDAS
# ()
# **
# * /
# + -


# Result will be seven as per given rules above
# print(3 * 3 + 3 / 3 - 3)

# Change something inside of above equation so that it can print 3 only
# print(3 * (3 + 3) / 3 - 3)

# Day 2 challenge BMI Calculator

# 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = int(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# bmi_result = weight/(height*height)
# We can also get the whole number by putting floor division //
# print(int(bmi_result))

# The type of below equation will be int but if we use single / then float
# print(8//7)



# Number manipulation and F strings in python
# Round the below number upto 2 decimal integers 
# print(round(3.14157, 2))

# Your life in weeks challenge

# age = int(input('What is your current age? \n'))
# total_age = 90

# remaining_years = 90 - age

# remaining_days = 365*remaining_years
# remaining_weeks = 52*remaining_years
# remaining_months = 12*remaining_years
# print(f'You have {remaining_days} days, {remaining_weeks} weeks & {remaining_months} months left')

# Tip Calculator challenge

print('Welcome to the tip calculator.\n')
bill = float(input('What was the total bill? $'))

tip = int(input('What percentage tip would you like to give? 10, 12, or 15? '))

people = int(input('How many people to split the bill? '))

tip_as_percent = tip/100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person,2)
print(f"Each person should pay {final_amount}")





