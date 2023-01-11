from google.cloud import dialogflow

from CustomConfigurations.AnswerRepositoryConfiguration import AnswerRepositoryConfiguration


class AnswerRepository:

    def __init__(self, answer_repository_configuration: AnswerRepositoryConfiguration):
        self.answer_repository_configuration = answer_repository_configuration

    def __del__(self):
        print("Answer repository object is destroyed.")

    def ask_question(self, question):
        session_client = dialogflow.SessionsClient()

        session = session_client.session_path(self.answer_repository_configuration.project_id,
                                              self.answer_repository_configuration.session_id)

        print("Session path: {}\n".format(session))

        text_input = dialogflow.TextInput(text=question,
                                          language_code=self.answer_repository_configuration.language_code)

        query_input = dialogflow.QueryInput(text=text_input)

        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )

        return response.query_result.fulfillment_text
