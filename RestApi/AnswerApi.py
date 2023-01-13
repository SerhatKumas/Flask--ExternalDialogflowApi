import uuid
from flask import request

from BusinessLayer.AnswerManager import AnswerManager
from CustomConfigurations.AnswerRepositoryConfiguration import AnswerRepositoryConfiguration
from DataAccessLayer.AnswerRepository import AnswerRepository

from app import app

project_id = "chatbotapiproject-dsnf"
session_id = str(uuid.uuid4())
language_code = "en-US"

answer_api_controller = AnswerManager(
    AnswerRepository(
        AnswerRepositoryConfiguration(
            project_id, session_id, language_code
        )
    )
)


@app.route('/ask-question')
def ask_question():
    question = request.args.get("question")
    answer = answer_api_controller.ask_question(question)
    return answer


@app.route('/display-repository-config')
def display_repository_config_information():
    answer = answer_api_controller.display_repository_config_information()
    return answer
