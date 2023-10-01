from question_model import Question
from data import Data
from quiz_brain import QuizBrain

question_bank = []
data = Data()
question_data = data.get_data()

for question in question_data:
    q = Question(text=question["question"], answer=question["correct_answer"])
    question_bank.append(q)


quiz_brain = QuizBrain(question_list=question_bank)


while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print(f"You're final score is {quiz_brain.score}/{quiz_brain.question_number}")