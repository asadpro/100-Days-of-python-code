# programming_dic = {
#         "bug":"a programming error",
#         "function":"a piece of code"
#         }
# print(programming_dic["bug"])

# # inserting data into dictionary

# programming_dic["loop"]="An action which repeat over and over again"

# # clearing data from dictionary
# # print(dic1)
# # one way to clear data from dictionary
# # dic1 = {}
# # Other way to clear data from dictionary
# # dic1.clear()
# # print(dic1)

# #   Edit an item in a dictionary
# programming_dic["bug"]="A programming error which prevents program from executing."

# print(programming_dic)

# # Loop through a dictionary
# for data in programming_dic:
#     i = 1
#     print(f"{i} Key of programming dictionary: ",data)
#     i=+1

# 👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇
# Grading program challenge
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.

# student_grades = {}
# for grades in student_scores:
#     scores = student_scores[grades]
#     if scores >=91 and scores <=100:
#         student_grades[grades] = "Outstanding"
    
#     elif scores >=81 and scores <=90:
#         student_grades[grades] = "Exceeds Expectations"
    
#     elif scores >=71 and scores <=80:
#         student_grades[grades] = "Acceptable"
    
#     else:
#         student_grades[grades] = "Fail"

# #TODO-2: Write your code below to add the grades to student_grades.👇

# # 🚨 Don't change the code below 👇
# print(student_grades)

# 👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇
# Dictionary challenge
# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #DO NOT change the code above 👆

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log.
# def add_new_country(name, visit_count, cities_visited):
#   new_country = {}
#   new_country["country"] = name
#   new_country["visits"] = visit_count
#   new_country["cities"] = cities_visited
#   travel_log.append(new_country)

# #Do not change the code below 👇
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

# 👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇👇

# Final progect of blind bid auction
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
terminate = False
print(logo)
print('Welcome to the secret auction program.')
bid_dictionary={}

def find_highest_bider(bidding_record):
    highest_bid = 0
    winner= ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder] 
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f'The winner is  {winner} with a bid of ${highest_bid}')


while not terminate:
    name = input('What is your name?: ')
    bid_amount = int(input('What is your bid?: $'))
    bid_dictionary[name] = bid_amount
    ask_to_end = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if ask_to_end == "no" or ask_to_end == "n":
        terminate = True


find_highest_bider(bidding_record=bid_dictionary)




