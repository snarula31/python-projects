from question_model import Question


class QuizBrain:
    def __init__(self, ques_list) -> None:
        self.ques_number = 0
        self.score = 0
        self.ques_list = ques_list

    def still_has_questions(self):
        return self.ques_number < len(self.ques_list)

    def next_ques(self):
        current_ques = self.ques_list[self.ques_number]
        self.ques_number += 1
        user_answer = input(
            f"Q{self.ques_number}. {current_ques.text} \n(True/False):")
        self.check_answer(user_answer, current_ques.ans)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")

        else:
            print("That's wrong")
            print(f"The correct answer is {correct_answer}")

        print(f"Your score: {self.score}/{self.ques_number}")
        print("\n")
