from question_model import Question
from data import Question_data
import os
from quiz_brain import QuizBrain

os.system('cls')

question_bank = []

questions = []

for question in Question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_ques = Question(question_text, question_answer)
    question_bank.append(new_ques)

# print(question_bank)
# print(Question_data)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_ques()

print("You've completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.ques_number}")
