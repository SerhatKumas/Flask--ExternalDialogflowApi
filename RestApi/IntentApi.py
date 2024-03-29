import uuid

import flask
from flask import request
import json

from BusinessLayer.AnswerManager import AnswerManager
from BusinessLayer.IntentManager import IntentManager
from CustomConfigurations.AnswerRepositoryConfiguration import AnswerRepositoryConfiguration
from CustomConfigurations.IntentRepositoryConfiguration import IntentRepositoryConfiguration
from DataAccessLayer.AnswerRepository import AnswerRepository
from DataAccessLayer.IntentRepository import IntentRepository
from app import app

# export GOOGLE_APPLICATION_CREDENTIALS="/Users/serhatkumas/Desktop/BasicExternalDialogflowApi/authentication.json"

# Project Configuration
project_id = "chatbotapiproject-dsnf"
session_id = str(uuid.uuid4())
language_code = "en-US"

# Manager Object (Business Layer) Creation
answer_api_controller = AnswerManager(
    AnswerRepository(
        AnswerRepositoryConfiguration(
            project_id, session_id, language_code
        )
    )
)

# Manager Object (Business Layer) Creation
intent_api_controller = IntentManager(
    IntentRepository(
        IntentRepositoryConfiguration(project_id)
    )
)


# Configuration display end point
@app.route('/display-intent-repository-config')
def display_intent_repository_config_information():
    answer = intent_api_controller.display_repository_config_information()
    return answer


# All intents chatbot has, display web page
@app.route('/all-intents-page', methods=["GET"])
def get_all_intents_page():
    return flask.render_template("IntentListPage.html")


# All intents chatbot has, display end point
@app.route('/get-all-intents')
def get_all_intents():
    answer = intent_api_controller.get_all_intents()
    return json.dumps(answer)


@app.route('/all-intents-page-info')
def get_all_intent_page_info():
    info = []
    answer = intent_api_controller.get_all_intents()
    for intent in answer:
        info.append(intent)
        info.append(answer_api_controller.ask_question(intent))
    return json.dumps(info)


# Creation of intent by json data end point
@app.route('/create-intent-by-json', methods=['POST'])
def create_intent_by_json():
    number_of_created_intents = 0
    intents = request.json.get("intents")
    for intent in intents:
        display_name = intent.get('display_name')
        training_phase = intent.get('training_phase').split(',')
        message_text = intent.get('message_text').split(',')
        intent_api_controller.create_intent(display_name, training_phase, message_text)
        number_of_created_intents += 1
    return "{} new intent is created".format(number_of_created_intents)


# Display name update end point
@app.route('/update-display-name')
def update_display_name():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json_data = request.get_json()
        display_name_from = json_data["display_name_from"]
        display_name_to = json_data["display_name_to"]
        answer = intent_api_controller.update_display_name_of_intent_by_display_name(display_name_from, display_name_to)
        return answer
    else:
        return 'Content-Type not supported!'


# Intent deletion end point
@app.route('/delete-intent')
def delete_intent_by_display_name():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json_data = request.get_json()
        display_name = json_data["display_name"]
        answer = intent_api_controller.delete_intent_by_display_name(display_name)
        return answer
    else:
        return 'Content-Type not supported!'
