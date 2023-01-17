# Flask--ExternalDialogflowApi


- It is REST Api project for dialogflow chatbot management and answer taking


- Chatbot structure is build in Google Dialogflow


- Currently, 2 api files are existed which are for chatbot answers and chatbot management 


- AnswerApi - AnswerManager - AnswerRepository is for client queries to chatbot


- IntentApi - IntentManager - IntentRepository is for management of intents (content) in chatbot


- AnswerRepositoryConfiguration is class for chatbot answer data access object


- IntentRepositoryConfiguration is class for chatbot intent management access object

## End Points

- /ask-question?question=(user-question)  => Asking question to chatbot (GET request)


- /display-answer-repository-config => Displaying configuration information of Data access object (GET request)


- /get-all-intents  => Displaying all intents chatbot has (GET request)


- /create-intent-by-json  => Creation of intent with Json file (POST request)

Example JSON :
{ "intents" : [{ "display_name":"Deneme5", "training_phase":"train1,train2,train3,train4", "message_text":"text1,tex4"},
{ "display_name":"Deneme6", "training_phase":"train1,train2,train3,train4", "message_text":"text1,text2,tex3,tex4"},
{ "display_name":"Deneme7", "training_phase":"train1,train2,train3,train4", "message_text":"text1,text2,tex3,tex4"},
{ "display_name":"Deneme8", "training_phase":"train1,train2,train3,train4", "message_text":"text1,text2,tex3,tex4"}]}

- /update-display-name?display_name_from=(old_display_name)&display_name_to=(new_display_name)  => Updating display name of intent (GET request)


- /delete-intent?display_name=(display_name) => Deletion of intent with display_name of intent (POST request)


- /display-intent-repository-config => Displaying configuration information of Data access object (GET request)


## Technologies

- [@Python](https://www.python.org/downloads/)

- [@Flask](https://www.python.org/downloads/)


## Test

- git clone https://github.com/SerhatKumas/Flask--ExternalDialogflowApi.git

- pip install <required-libraries>

- Enter "flask run" to terminal

## Referance

- [@Google-apis / dialogflow](https://github.com/googleapis/python-dialogflow)


# Hi, I'm Serhat the Author! 👋

## 🔗 Connection Links

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/serhatkumas/)

[![@Github](https://img.shields.io/badge/github-0A66C2?style=for-the-badge&logo=github&logoColor=white)](https://www.github.com/serhatkumas)