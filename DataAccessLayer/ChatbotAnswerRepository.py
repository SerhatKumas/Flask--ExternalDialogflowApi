from google.cloud import dialogflow


class ChatbotRepository:

    def __init__(self, project_id, session_id, language_code):
        self.project_id = project_id
        self.session_id = session_id
        self.language_code = language_code

    def __del__(self):
        print("Chatbot answer repository object is destroyed.")

    def send_message(self, message):
        session_client = dialogflow.SessionsClient()

        session = session_client.session_path(self.project_id, self.session_id)

        print("Session path: {}\n".format(session))

        text_input = dialogflow.TextInput(text=message, language_code=self.language_code)

        query_input = dialogflow.QueryInput(text=text_input)

        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )

        return response.query_result.fulfillment_text
