class OpenAiRepositoryConfiguration:
    # Configuration parameters injection
    def __init__(self, api_key):
        self.api_key = api_key

    def __del__(self):
        print("Open Ai repository configuration object is destroyed.")
