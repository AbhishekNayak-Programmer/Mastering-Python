from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for element in question_data :
    question_bank.append(Question(element["text"], element["answer"]))

quiz = QuizBrain(question_bank)

while quiz.quiz_still_has_questions :
    quiz.next_question()

print(f"You have completed the quiz! your final score was: {quiz.score}/{quiz.question_number}")