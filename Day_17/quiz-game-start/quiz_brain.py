class QuizBrain :
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    # Asking Question   
    def next_question(self) :
        question = self.question_list[self.question_number]
        self.question_number += 1
        option = input(f"Q.{self.question_number}: {question.text} (True/False)?: ")
        self.checkAnswer(option, question.answer)

    # Checking answer
    def checkAnswer(self, option_selected, correct_answer) :
        if option_selected.lower() == correct_answer.lower() :
            print("Ypu got it right!")
            self.score += 1
        else :
            print("That's Wrong")
        
        print(f"The correct answer was : {correct_answer}")
        print(f"Your current score is : {self.score}/{self.question_number} \n")

    # Checking is End 
    @property
    def quiz_still_has_questions(self) :
        if self.question_number < len(self.question_list) :
            return True
        return False
           