import random

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
user_score = 0
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(text=question_text,answer=question_answer)
    question_bank.append(new_question)


print("Welcome True or False Game: Start")

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.nex_question()
print('You have completed the quiz')
print(f'Your final score is {quiz.score}/{quiz.question_number}')