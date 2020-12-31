
class QuizBrain:

    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions
        self.score = 0

    def still_has_questions(self):
        """Checks if there are still questions left"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """prompts the question to the user and asks for their answers"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)? ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right! 👍")
        else:
            print(f"Your answer is wrong 😔, the correct answer is '{correct_answer}'.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
