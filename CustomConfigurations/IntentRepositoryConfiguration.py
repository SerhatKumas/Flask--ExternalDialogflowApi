from google.cloud import dialogflow


class IntentRepositoryConfiguration:
    # Configuration parameters injection
    def __init__(self, project_id):
        self.project_id = project_id
        self.agent_parent = dialogflow.AgentsClient.agent_path(project_id)
        self.intents_client = dialogflow.IntentsClient()

    def __del__(self):
        print("Intent repository configuration object is destroyed.")
