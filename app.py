from flask import Flask

app = Flask(__name__)

# Import for connecting api file to flask app
# export GOOGLE_APPLICATION_CREDENTIALS="/Users/serhatkumas/Desktop/BasicExternalDialogflowApi/authentication.json"
import RestApi.AnswerApi
import RestApi.IntentApi

# Flask app starter
if __name__ == '__main__':
    app.run()
