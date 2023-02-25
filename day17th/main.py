from question_model import Question
from data import question_data

question_bank = []

for item in question_data:
    q = item['text']
    a = item['answer']

    new_question = Question(q, a)
    question_bank.append(new_question)



