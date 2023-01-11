import uuid
from flask import request
from DataAccessLayer.ChatbotAnswerRepository import ChatbotRepository
from app import app

project_id = "chatbotapiproject-dsnf"
session_id = str(uuid.uuid4())
language_code = "en-US"

api_controller = ChatbotRepository(project_id, session_id, language_code)


@app.route('/ask-question')
def send_message():
    print('send message')
    message = request.args.get("message")
    answer = api_controller.send_message(message)
    return answer
