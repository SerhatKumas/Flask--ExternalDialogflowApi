import uuid
from flask import request

from BusinessLayer.AnswerManager import AnswerManager
from BusinessLayer.IntentManager import IntentManager
from CustomConfigurations.AnswerRepositoryConfiguration import AnswerRepositoryConfiguration
from CustomConfigurations.IntentRepositoryConfiguration import IntentRepositoryConfiguration
from DataAccessLayer.AnswerRepository import AnswerRepository

from BusinessLayer.OpenAiManager import OpenAiManager
from CustomConfigurations.OpenAiRepositoryConfiguration import OpenAiRepositoryConfiguration
from DataAccessLayer.IntentRepository import IntentRepository
from DataAccessLayer.OpenAiRepository import OpenAiRepository

from app import app

# Project Configuration
project_id = "chatbotapiproject-dsnf"
session_id = str(uuid.uuid4())
language_code = "en-US"
api_key = ""
default_fallback_content = ["I didn't get that. Can you say it again?", "I missed what you said. What was that?",
                            "Sorry, could you say that again?", "Sorry, can you say that again?",
                            "Can you say that again?", "Sorry, I didn't get that. Can you rephrase?",
                            "Sorry, what was that?", "One more time?", "What was that?", "Say that one more time?",
                            "I didn't get that. Can you repeat?", "I missed that, say that again?"]

# Manager Object (Business Layer) Creation
answer_api_controller = AnswerManager(
    AnswerRepository(
        AnswerRepositoryConfiguration(
            project_id, session_id, language_code
        )
    )
)

# Manager Object (Business Layer) Creation for Open Ai Api
openai_api_controller = (
    OpenAiManager(
        OpenAiRepository(
            OpenAiRepositoryConfiguration(api_key)
        )
    )
)

# Manager Object (Business Layer) Creation
intent_api_controller = IntentManager(
    IntentRepository(
        IntentRepositoryConfiguration(project_id)
    )
)


# Question asking end point
@app.route('/ask-question')
def ask_question():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.get_json()
        question = json["question"]
        answer = answer_api_controller.ask_question(question)
        if answer in default_fallback_content:
            answer = openai_api_controller.ask_question(question)
            intent_api_controller.create_intent(question, [question], [answer])
        return answer
    else:
        return 'Content-Type not supported!'


# Configuration display end point
@app.route('/display-answer-repository-config')
def display_answer_repository_config_information():
    answer = answer_api_controller.display_repository_config_information()
    return answer
