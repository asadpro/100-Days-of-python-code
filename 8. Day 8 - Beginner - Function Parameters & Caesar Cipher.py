# def greet():
#     print("Hello python")
#     print("Hello python")
#     print("Hello python")
# greet()

# def nameLoc(name, location):
#     print("How are you",name)
#     print("For how long you have been living in ",location)

# nameLoc(name="Asad",location="Fattu abdurrahima peshawar")

# 👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇

#Write your code below this line 👇

# from math import ceil


# def paint_calc(height,width,cover):
#     cans = (height*width)/cover
#     print(f"You'll need {ceil(cans)} cans of paint.")


# #Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.   


# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

# 👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇
#Write your code below this line 👇

# def prime_checker(number):
#     is_prime = True
#     for i in range(2,number-1):
#         if number%i==0:
#             is_prime = False
#     if is_prime:
#         print("It's a prime number")
#     else:
#         print("it's not prime number")

# #Write your code above this line 👆
    
# #Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)

# 👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇

# Final Caesar Cipher Challenge
from operator import contains
from turtle import goto


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


symbols = [ "~","`","!","@","#","£","€","$","¢","¥","§","%","°","^","&","*","(",")","-","_","+","=","{","}","[","]","|","/",":",";","'","<",">",",","."
,"~","`","!","@","#","£","€","$","¢","¥","§","%","°","^","&","*","(",")","-","_","+","=","{","}","[","]","|","/",":",";","'","<",">",",","."]
terminate = False
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text: #"asad1234"
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    
        if char not in alphabet and char!=" ":
            for symbol in char:
                pos_symbol = symbols.index(symbol)
                symbol_new_pos = pos_symbol + shift_amount
                end_text += symbols[symbol_new_pos]
            # end_text += char
        elif char == " ":
            end_text += " "
        else:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
    
  print(f"Here's the {cipher_direction}d result: {end_text}")



#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
while terminate!= True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift%25
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    response = input('Type \'yes\' if you want to go again? Otherwise type \'no\' ')
    if response == "no" or response == 'n':
        terminate = True
        print('Goodbye😍💡💡😍')


#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).

















