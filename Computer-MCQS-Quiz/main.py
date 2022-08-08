import data
from question_model import Question
from quiz_hall import *

data_file = data.actual_data

question_bank = []

for data_item in data_file["results"]:

    question_text = data_item["question"]
    question_answer = data_item["correct_answer"]
    new_question = Question(text=question_text, answer=question_answer)
    question_bank.append(new_question)

quiz = Quiz(question_list=question_bank)

while quiz.still_has_question():
    quiz.next_question()
