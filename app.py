from flask import Flask

app = Flask(__name__)

# Import for connecting end point to flask app runner
import RestApi.AnswerApi
import RestApi.IntentApi
import RestApi.ScrapyApi

# Flask app starter
if __name__ == '__main__':
    app.run()
