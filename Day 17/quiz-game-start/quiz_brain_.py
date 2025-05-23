class QuizBrain:
    def __init__(self,list):
        self.score = 0
        self.question_number = 0
        self.question_list = list

    def next_question(self):
        text = self.question_list[self.question_number].text
        answer = self.question_list[self.question_number].answer
        self.question_number += 1
        user_answer = input(f"q.{self.question_number}: {text} (True/False)?: ")
        self.check_answer(user_answer,answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got is wrong.")
        print(f"The correct answer was : {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
