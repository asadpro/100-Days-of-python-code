# import random

# integers = []
# floating = []
# for i in range(3):
#     integers.append(random.randint(50,55)) 
#     floating.append(random.random())

# print(integers)
# print(floating)

# ==========================================
# Challenge of Heads or Tails

#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲


# Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# import random
# index_of_name = random.randint(0,len(names)-1)

# print(f'{names[index_of_name]} is going to buy the meal today!')
 

# ==========================================
# Challenge of Treasure Map

# 🚨 Don't change the code below 👇
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")

# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# horizontal = int(position[1]) #2
# vertical = int(position[0]) #3
# print(map)

# # selected_row = map[vertical - 1]
# # selected_row[horizontal - 1] = "X"

# map[vertical-1][horizontal - 1] = "X "





# #Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")


# ==========================================
# Final project of Rock, Paper & Scissors

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")

####### Debugging challenge: #########
#Try running this code and type 5.
#It will give you an IndexError and point to line 32 as the issue.
#But on line 38 we are trying to prevent a crash by detecting
#any numbers great than or equal to 3 or less than 0.
#So what's going on?
#Can you debug the code and fix it?
#Solution: https://repl.it/@appbrewery/rock-paper-scissors-debugged-end


