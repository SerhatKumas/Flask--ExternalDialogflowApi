from DataAccessLayer.IntentRepository import IntentRepository


class IntentManager:

    # Intent repository object constructor injection
    def __init__(self, intent_repository: IntentRepository):
        self.intent_repository = intent_repository

    def __del__(self):
        print("Intent manager object is destroyed.")

    # Configuration display method
    def display_repository_config_information(self):
        try:
            answer = self.intent_repository.display_repository_config_information()
            return answer
        except Exception as e:
            print(e)
            return e

    # All intents chatbot has, display method
    def get_all_intents(self):
        try:
            answer = self.intent_repository.get_all_intents()
            return answer
        except Exception as e:
            print(e)
            return e

    # Creation of intent method
    def create_intent(self, display_name, user_training_phrases_parts, message_texts):
        try:
            answer = self.intent_repository.create_intent(display_name, user_training_phrases_parts, message_texts)
            return answer
        except Exception as e:
            print(e)
            return e

    # Display name update method
    def update_display_name_of_intent_by_display_name(self, display_name_from, display_name_to):
        try:
            answer = self.intent_repository.update_display_name_of_intent_by_display_name(display_name_from, display_name_to)
            return answer
        except Exception as e:
            print(e)
            return e

    # Intent deletion method
    def delete_intent_by_display_name(self, display_name):
        try:
            answer = self.intent_repository.delete_intent_by_display_name(display_name)
            return answer
        except Exception as e:
            print(e)
            return e

    def get_intent_id_by_display_name(self, display_name):
        try:
            answer = self.intent_repository.get_intent_id_by_display_name(display_name)
            return answer
        except Exception as e:
            print(e)
            return e
