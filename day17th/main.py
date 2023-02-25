from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    q = item['question']
    a = item['correct_answer']

    new_question = Question(q, a)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_have_questions():
    quiz.next_question()


print("You've completed the quiz! ")
print(f"Your final score was {quiz.score}/{quiz.question_number}")

