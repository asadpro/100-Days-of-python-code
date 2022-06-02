# =========================================
# print('Welcom to the rollercoaster!\n')
# height = int(input('What is your height in cm? '))

# if height >= 120:
#     print('You can ride')
#     age = int(input('What is your age?  '))
#     if(age>=12 & age<=18):
#         bill = 7
#         print('pay $7')
#     elif(age<12):
#         bill = 5
#         print('pay $5')
#     else:
#         bill = 12
#         print("pay $12")

#     wants_photo = input('Do you want a photo taken? Y or N.')
#     if (wants_photo == 'y'):
#         bill +=3
#     print(f'Your final bill is ${bill}')
# else:
#     print(f'You have to grow taller than {height} then you can ride')


# =========================================
# challenge of Odd or Even number
# num = int(input('Enter a number to check whether it\'s Odd or Even: '))

# if num%2==0:
#     print(f'{num} is Even number')
# else:
#     print(f'{num} is Odd number')

# =========================================
# Challenge of BMI Calculator 2.1
"""Write a program that interprets the Body Mass Index 
(BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based
on the BMI value.

Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.
https://cdn.fs.teachablecdn.com/qTOp8afxSkGfU5YGYf36

The BMI is calculated by dividing a person's weight 
(in kg) by the square of their height (in m):

https://cdn.fs.teachablecdn.com/jKHjnLrNQjqzdz3MTMyv

Warning you should round the result to the nearest whole number. 
The interpretation message needs to include the words in bold from 
the interpretations above. e.g. underweight, normal weight, overweight, 
obese, clinically obese."""

# height = float(input('What is your height in meter? '))
# weight = int(input('What is your weight in Kg? '))

# bmi = round(weight/(height*height),1)
# print(bmi)
# if (bmi<18.5):
#     print(f"Your BMI is {bmi}, you are underweight.")
# elif (bmi>18.5 and bmi<=25):
#     print(f"Your BMI is {bmi}, you have a normal weight.")
# elif (bmi>25 and bmi<=30):
#     print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif (bmi>30 and bmi<=35):
#     print(f"Your BMI is {bmi}, you are obese.")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese.")


# =========================================
# Create this program using the following flowchart
# https://viewer.diagrams.net/?target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Leap%20Algorithm#R7VpNc9owEP01HNuxJdmYY4CkzTTNdEpmmhyFrdhqhcXIIkB%2BfSUsY4wcQhqwC%2B0p0urDu29Xu08KHTiYLD4JPE2%2B8oiwDnCiRQcOOwC4CPjqj5Ysc0k3gLkgFjQyk0rBiD4TI3SMdEYjklUmSs6ZpNOqMORpSkJZkWEh%2BLw67ZGz6lenOCaWYBRiZkt/0EgmuTQA3VL%2BmdA4Kb7s%2Br18ZIKLycaSLMERn2%2BI4GUHDgTnMm9NFgPCNHgFLvm6qxdG14oJksp9FoDbYTJlQFxPomj0Jbzr4tT9YJTN5LIwmETKftPlQiY85ilml6W0L/gsjYje1VG9cs4N51MldJXwJ5FyaZyJZ5IrUSInzIwqhcXyXq//6BXdB7PdqjNcVHpL08t11Qq%2BCIERZXwmQrLD7iKUsIiJ3DEPrB2lIpzwCVH6qHWCMCzpU1UPbEItXs8rvaEaxiFvcI7Z9wmzmfnS6O7i%2B53lstIhGt15QiUZTfHK/rk6lVXwzZ5ESLLYDaNttlkAYE85brVoWZxWE%2BTz8oy4xRFONs4Hco6ElfePBjLYM5DhOwN5tfRCCLzcmDDlNJXZxs7ftKAMFLcLtgKlyOulq/M9S8evlfvzWPD/x8LOWHCdQwSD5W3kdre97W8d91w1s64Mg7fGFQLWl5qIK2Dl4%2BtMr9GahYzglGkjOsBnCv3%2BWKhWrFsRfaIZHas4A85YT0EdeGVn8YRPxrOsmQxe8Jcif3dr8jf07PwdHCt/QwvbW65xvSHK/HcVvEfK2IAzLlZr4WMQkjBU8kwK/otsjIwDD3nOYQB23SrA65PQWoHs1gBsAasMllX0MKNxqtqhMpwooPoaFqr48YUZmNAoyjMoyegzHq%2B20iiaQ6z29fodb6j3Ukkzy/PngeLYDSwm0rOBhjU4g2PhHFg4P5Ds5IGG/j5AoyaBdmErZX5B5X1RyFX7oaz4qlfWeN0pSvxfQA2KVPM6N2j3xhO06VP3XH2KWvWpcyjapG%2BZLRMn6IPX63pdvTkacXJtVnpwzhR5JIhQHWcKwBj6/oFIqVfFFtaR0kY5E2jnVeFESwzaMx2BVtMRaOd14ERLzL4%2BdXutlhh0qBKD2i8xyNum2rWJsI5rH6/I9M6lyHi9bXRRzUWm4TJjM6RzuDOi3hZXClq%2BMRYmnNcbCHS3I7oO6EbfQIDNSc8AaGQBDdt%2BbAL2s%2Bk5ZA47Sdch3WzusCnGST9QQ9RkHVTd8ocO%2Bb9jyp%2BLwMvf

# Challenge of Leap year
# year = int(input('Enter year: '))
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print('Leap Year')
#         else:
#             print('Not Leap Year')
#     else:
#         print("Leap Year")
# else:
#     print('Not Leap Year')


# =========================================
# challenge of Pizza Deliveries

# 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# S_Pizza = 15
# M_Pizza = 20
# L_Pizza = 25
# bill = 0

# if size == 's':
#     bill+=15
#     if add_pepperoni == 'y':
#         bill+=2
#         if extra_cheese == 'y':
#             bill+=1
#     print(f'Your final bill is: ${bill}')

# elif size == 'm':
#     bill+=20
#     if add_pepperoni =='y':
#         bill+=3
#         if extra_cheese == 'y':
#             bill+=1
#     print(f'Your final bill is: ${bill}')

# elif size == 'l':
#     bill+=25
#     if add_pepperoni =='y':
#         bill+=3
#         if extra_cheese == 'y':
#             bill+=1
#     print(f'Your final bill is: ${bill}')

# else:
#     print('You have put the wrong character!!!')


# =========================================
# challenge of Love calculator

# 🚨 Don't change the code below 👇

# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n").lower()
# name2 = input("What is their name? \n").lower()
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# combine_name = name1+name2

# t = combine_name.count('t')
# r = combine_name.count('r')
# u = combine_name.count('u')
# e = combine_name.count('e')

# total_true = t+r+u+e


# l = combine_name.count('l')
# o = combine_name.count('o')
# v = combine_name.count('v')
# e = combine_name.count('e')

# total_love = l+o+v+e
# love_score = int(str(total_true) + str(total_love))


# if love_score<10 or love_score>90:
#     print(f"Your score is {love_score}, you go together like coke and mentos.")
# elif love_score>40 and love_score<50:
#     print(f"Your score is {love_score}, you are alright together.")
# else:
#     print(f"Your score is {love_score}.")


# =========================================
# Challenge of Tresure Island
print(
    '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇

direction = input(
    'You\'re at a crossroad. Where do you want to go? Type "left" or "right" '
).lower()

if direction == "left" or direction == "l":
    swim_wait = input(
        'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. '
    ).lower()
    if swim_wait == "wait" or swim_wait == "w":
        which_door = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? "
        ).lower()
        if which_door == "red":
            print("Burned by fire Game Over")
        elif which_door == "yellow":
            print("You Win!")
            print(
                """
    _                  _                   ____       _        
   / \   ___  __ _  __| |_ __  _ __ ___   | __ )  ___| |_ __ _ 
  / _ \ / __|/ _` |/ _` | '_ \| '__/ _ \  |  _ \ / _ \ __/ _` |
 / ___ \\__ \ (_| | (_| | |_) | | | (_) | | |_) |  __/ || (_| |
/_/   \_\___/\__,_|\__,_| .__/|_|  \___/  |____/ \___|\__\__,_|
                        |_|                                    
            """
            )
        elif which_door == "blue":
            print("Eaten by beasts. Game Over")
        else:
            print("Game Over")
    else:
        print("Game Over.")


else:
    print("You have fall into a hole Game Over.")
