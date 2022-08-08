class Quiz:
    def __init__(self, question_list):

        self.score = 0
        self.question_no = 0
        self.question_list = question_list

    def still_has_question(self):
        return self.question_no < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no +=1
        user_answer = input(f'Q:{self.question_no} {current_question.text} (True/False)?: ')
        self.check_answer(userAnswer=user_answer, correctAnswer=current_question.answer)

    
    def check_answer(self, userAnswer, correctAnswer):
        if userAnswer.lower() == correctAnswer.lower():
            self.score +=1
            print('You got it right! ')
        else:
            print('You got it wrong!')
        print(f'The correct answer was: {correctAnswer}')
        print(f'Your current score is: {self.score}/{self.question_no}')

        