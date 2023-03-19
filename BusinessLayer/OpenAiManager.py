from DataAccessLayer.OpenAiRepository import OpenAiRepository


class OpenAiManager:

    # OpenAi repository object constructor injection
    def __init__(self, openai_repository: OpenAiRepository):
        self.openai_repository = openai_repository

    def __del__(self):
        print("Open Ai manager object is destroyed.")

    '''
    # Configuration display method
    def display_repository_config_information(self):
        try:
            answer = self.openai_repository.display_repository_config_information()
            return answer
        except Exception as e:
            print(e)
            return e
            
    '''

    # Question asking method
    def ask_question(self, question):
        try:
            answer = self.openai_repository.ask_question(question)
            return answer
        except Exception as e:
            print(e)
            return e

