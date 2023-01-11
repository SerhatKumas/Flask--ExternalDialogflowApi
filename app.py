from flask import Flask

app = Flask(__name__)

# Import for connecting api file to flask app
import RestApi.AnswerApi

# Flask app starter
if __name__ == '__main__':
    app.run()