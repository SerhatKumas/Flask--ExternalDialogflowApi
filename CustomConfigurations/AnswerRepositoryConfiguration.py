class AnswerRepositoryConfiguration:
    # Configuration parameters injection
    def __init__(self, project_id, session_id, language_code):
        self.project_id = project_id
        self.session_id = session_id
        self.language_code = language_code

    def __del__(self):
        print("Answer repository configuration object is destroyed.")
