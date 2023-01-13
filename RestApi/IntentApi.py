from flask import request

from BusinessLayer.IntentManager import IntentManager
from CustomConfigurations.IntentRepositoryConfiguration import IntentRepositoryConfiguration
from DataAccessLayer.IntentRepository import IntentRepository
from app import app

project_id = "chatbotapiproject-dsnf"

intent_api_controller = IntentManager(
    IntentRepository(
        IntentRepositoryConfiguration(project_id)
    )
)


@app.route('/display-intent-repository-config')
def display_intent_repository_config_information():
    answer = intent_api_controller.display_repository_config_information()
    return answer


@app.route('/get-all-intents')
def get_all_intents():
    answer = intent_api_controller.get_all_intents()
    return answer


# End point will be written when implementation is available
def create_intent(display_name, user_training_phrases_parts, message_texts):
    # Not implemented for user interface
    answer = intent_api_controller.create_intent(display_name, user_training_phrases_parts, message_texts)
    return answer


@app.route('/update-display-name')
def update_display_name():
    display_name_from = request.args.get("display_name_from")
    display_name_to = request.args.get("display_name_to")
    answer = intent_api_controller.update_display_name_of_intent_by_display_name(display_name_from, display_name_to)
    return answer


@app.route('/delete-intent')
def delete_intent_by_display_name():
    display_name = request.args.get("display_name")
    answer = intent_api_controller.delete_intent_by_display_name(display_name)
    return answer

