from DataAccessLayer.AnswerRepository import AnswerRepository


class AnswerManager:

    # Answer repository object constructor injection
    def __init__(self, answer_repository: AnswerRepository):
        self.answer_repository = answer_repository

    def __del__(self):
        print("Answer manager object is destroyed.")

    # Configuration display method
    def display_repository_config_information(self):
        try:
            answer = self.answer_repository.display_repository_config_information()
            return answer
        except Exception as e:
            print(e)
            return e

    # Question asking method
    def ask_question(self, question):
        try:
            answer = self.answer_repository.ask_question(question)
            return answer
        except Exception as e:
            print(e)
            return e
