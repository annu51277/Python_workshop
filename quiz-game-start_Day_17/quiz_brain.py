class QuizBrain:

    def __init__(self,q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_question(self):
        no_of_questions = len(self.question_list)
        return self.question_number < no_of_questions

    def nex_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        user_choice = input(f"Q.{self.question_number} {current_question.text} is the True/False: ")
        self.check_answer(user_choice,current_question.answer)


    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f'You are Right and your score is {self.score}/{self.question_number}')

        else:
            print(f'Opps ! You are wrong and your score is {self.score}/{self.question_number}')
            print(f"The correct answer was {correct_answer}")


