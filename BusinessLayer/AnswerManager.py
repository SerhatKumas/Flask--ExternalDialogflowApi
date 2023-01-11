from DataAccessLayer.AnswerRepository import AnswerRepository


class AnswerManager:

    def __init__(self, answer_repository: AnswerRepository):
        self.answerRepository = answer_repository

    def __del__(self):
        print("Answer manager object is destroyed.")

    def ask_question(self, question):
        answer = self.answerRepository.ask_question(question)
        return answer
