from DataAccessLayer.AnswerRepository import AnswerRepository


class AnswerManager:

    def __init__(self, answer_repository: AnswerRepository):
        self.answerRepository = answer_repository

    def __del__(self):
        print("Answer manager object is destroyed.")

    def display_repository_config_information(self):
        try:
            answer = self.display_repository_config_information()
            return answer
        except Exception as e:
            print(e)
            return e + " Answer Management Error"

    def ask_question(self, question):
        try:
            answer = self.answerRepository.ask_question(question)
            return answer
        except Exception as e:
            print(e)
            return e + " Answer Management Error"
