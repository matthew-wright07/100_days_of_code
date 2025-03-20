class QuizBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        item = self.question_list[self.question_number]
        self.question_number += 1
        response = input(f"Q.{self.question_number}: {item.text} (True/False)\n")
        self.check_answer(response,item.answer)

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self,user_input,answer):
        if user_input.lower() == answer.lower():
            print("You got it")
            self.score += 1
        else:
            print("That is wrong")
        print(f"The correct answer was {answer}")
        print(f"Your score is {self.score}/{self.question_number}\n")
