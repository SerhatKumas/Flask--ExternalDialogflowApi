from google.cloud import dialogflow
from google.protobuf import field_mask_pb2

from CustomConfigurations.IntentRepositoryConfiguration import IntentRepositoryConfiguration


class IntentRepository:
    def __init__(self, intent_repository_configuration: IntentRepositoryConfiguration):
        self.intent_repository_configuration = intent_repository_configuration

    def __del__(self):
        print("Intent repository object is destroyed.")

    def display_repository_config_information(self):
        project_id = "Project id : " + self.intent_repository_configuration.project_id
        agent_parent = "Agent parent info :  " + self.intent_repository_configuration.agent_parent.__str__()
        intents_client = "Intents client info :  " + self.intent_repository_configuration.intents_client.__str__()

        return project_id + " /// " + agent_parent + " /// " + intents_client

    def get_all_intents(self):
        intents_client = self.intent_repository_configuration.intents_client
        parent = self.intent_repository_configuration.agent_parent
        intents = intents_client.list_intents(request={"parent": parent})
        intent_array = []
        for intent in intents:
            print("=" * 20)
            print("Intent name: {}".format(intent.name))
            print("Intent display_name: {}".format(intent.display_name))
            print("Action: {}\n".format(intent.action))
            print("Root followup intent: {}".format(intent.root_followup_intent_name))
            print("Parent followup intent: {}\n".format(intent.parent_followup_intent_name))
            intent_array.append(intent.display_name)

        return intent_array

    def create_intent(self, display_name, user_training_phrases_parts, message_texts):
        intents_client = self.intent_repository_configuration.intents_client
        parent = self.intent_repository_configuration.agent_parent
        training_phrases_upload = []
        for phrases_part in user_training_phrases_parts:
            part = dialogflow.Intent.TrainingPhrase.Part(text=phrases_part)
            training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
            training_phrases_upload.append(training_phrase)

        text = dialogflow.Intent.Message.Text(text=message_texts)
        message = dialogflow.Intent.Message(text=text)
        intent = dialogflow.Intent(
            display_name=display_name, training_phrases=training_phrases_upload, messages=[message]
        )

        response = intents_client.create_intent(
            request={"parent": parent, "intent": intent}
        )
        return "Intent created: {}".format(response)

    def update_display_name_of_intent_by_display_name(self, display_name_from, display_name_to):
        intents_client = self.intent_repository_configuration.intents_client
        intent = self.get_intent_by_display_name(display_name_from)
        intent.display_name = display_name_to
        update_mask = field_mask_pb2.FieldMask(paths=["display_name"])
        intents_client.update_intent(intent=intent, update_mask=update_mask)
        return "{} intent name is changed to {}".format(display_name_from, display_name_to)

    def delete_intent_by_display_name(self, display_name):
        intents_client = self.intent_repository_configuration.intents_client
        intent = self.get_intent_by_display_name(display_name)
        intents_client.delete_intent(request={"name": intent.name})
        return "{} intent is deleted".format(intent.display_name)

    def get_intent_by_display_name(self, display_name):
        intents_client = self.intent_repository_configuration.intents_client
        parent = self.intent_repository_configuration.agent_parent
        intents = intents_client.list_intents(request={"parent": parent})
        for intent in intents:
            if intent.display_name == display_name:
                return intent
