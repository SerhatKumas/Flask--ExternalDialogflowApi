from DataAccessLayer.IntentRepository import IntentRepository
from WebScrapyLevel.ScraperCryptoCom import scrape_crypto_com


class ScrapyManager:

    def __init__(self, intent_repository: IntentRepository):
        self.intent_repository = intent_repository

    def __del__(self):
        print("Scrapy manager object is destroyed.")

    def display_repository_config_information(self):
        try:
            answer = self.intent_repository.display_repository_config_information()
            return answer
        except Exception as e:
            print(e)
            return e

    def scrap_crypto_com(self):
        intent_array = scrape_crypto_com()
        return intent_array

    def create_content_by_scraped_data(self, array):
        temp_array_train = []
        temp_array_intent_response = []
        count = 0
        try:
            for counter in range(0, len(array), 2):
                if len(array[counter+1]) <= 300 \
                        and self.intent_repository.get_intent_by_display_name(array[counter]) is None:
                    count += 1
                    temp_array_train.append(array[counter])
                    temp_array_intent_response.append(array[counter + 1])
                    self.intent_repository.create_intent(array[counter], temp_array_train, temp_array_intent_response)
                temp_array_train = []
                temp_array_intent_response = []
            return count + " intent is added to project."
        except Exception as e:
            print(e)
            return e
