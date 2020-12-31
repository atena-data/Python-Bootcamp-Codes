from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for q in question_data:
    new_q = Question(q["text"], q["answer"])
    question_bank.append(new_q)


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("Congratulations! You completed the quiz.")
print(f"Your final score is: {quiz.score} out of {quiz.question_number}")
