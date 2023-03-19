import openai

from CustomConfigurations import OpenAiRepositoryConfiguration


class OpenAiRepository:

    # Answer repository configuration object constructor injection
    def __init__(self, openai_repository_configuration: OpenAiRepositoryConfiguration):
        openai.api_key = openai_repository_configuration.api_key
        self.openai_repository_configuration = openai_repository_configuration

    def __del__(self):
        print("Open Ai repository object is destroyed.")


    # Configuration display method
    '''
    def display_repository_config_information(self):
        api_key = "Api key : " + self.openai_repository_configuration.api_key

        return api_key + " /// "
    '''

    def ask_question(self, question):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=question,
            temperature=0,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
        print(response)
        return response.choices[0].text
