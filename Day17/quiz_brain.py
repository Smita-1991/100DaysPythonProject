class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.userScore = 0

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        return False

    def check_answer(self,answer,current_answer):
        if current_answer == answer:
            print("You got it right!")
            self.userScore +=1
        else:
            print("That's wrong.")
            print(f"The correct answer was: {current_answer}")
        print(f"Your current score is: {self.userScore}/{self.question_number}")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer=input(f"Q. {self.question_number}: {current_question.text} (True/False):")
        self.check_answer(user_answer,current_question.answer)