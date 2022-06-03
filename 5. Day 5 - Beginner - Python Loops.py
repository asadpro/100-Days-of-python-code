# ====================================
# Challenge of Average Height

# student_heights = input('Input list of the student heights: ').split()

# sum = 0
# counter = 0
# if len(student_heights) != 0:
#     for height in student_heights:
#         counter+=1
#         sum +=int(height)
#     result = int(sum/counter)
#     print('Average student height is: ',result)
# else:   
#     print('Your list is Empty. Please put some names into it.')


# ====================================
# Challenge of Highest Score in a list

# student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

# student_scores = input('Input scores: ').split()
# greater = 0
# for large in student_scores:
#     for num in student_scores:
#         if num>large:
#             greater = num

# print('The highest score in the class is: ',greater)


# ====================================
# Challenge of Adding Evens
# sum = 0
# for even in range(2,101,2):
#     sum +=even
# print("Sum of all even numbers are: ",sum) 


# ====================================
# Challenge of FizzBuzz

# for number in range(1,101):
#     if number%3 == 0 and number%5==0:
#         print('FizzBuzz')
#     elif number%3==0 and number%5!=0:
#         print('Fizz')
#     elif number%5==0 and number%3!=0:
#         print('Buzz')
#     else:
#         print(number)



# ====================================
# Challenge of password-generator-start
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# print(nr_letters)
# print(nr_symbols)
# print(nr_numbers)


# =============================
# Easy level of password generator without randomization 


password = ''

for char in range(1, nr_letters+1):
    password +=random.choice(letters)

for char in range(1,nr_symbols+1):
    password +=random.choice(numbers)

for char in range(1, nr_symbols+1):
    password +=random.choice(symbols)

print('Password without randomization: ',password)


# =============================
# Hard level of password generator with randomization 

password_list= []
new_password = ''


for char in range(1, nr_letters+1):
    password_list.append(random.choice(letters))

for char in range(1,nr_symbols+1):
    password_list.append(random.choice(numbers))

for char in range(1, nr_symbols+1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

for char in range(0,len(password_list)-1):
    new_password +=password_list[char]

print('password with randomization: ',new_password)






#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

