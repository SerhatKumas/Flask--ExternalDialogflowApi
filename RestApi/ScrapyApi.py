from BusinessLayer.ScrapyManager import ScrapyManager
from CustomConfigurations.IntentRepositoryConfiguration import IntentRepositoryConfiguration
from DataAccessLayer.IntentRepository import IntentRepository
from app import app

# Project Configuration
project_id = "chatbotapiproject-dsnf"

# Manager Object (Business Layer) Creation
scrape_api_controller = ScrapyManager(
    IntentRepository(
        IntentRepositoryConfiguration(project_id)
    )
)


# Configuration display end point
@app.route('/display-scrapy-level-config')
def display_scrapy_level_config_information():
    answer = scrape_api_controller.display_repository_config_information()
    return answer


@app.route('/crypto-com-scrapy')
def create_intent_by_crypto_com_scrape():
    array = scrape_api_controller.scrap_crypto_com()
    answer = scrape_api_controller.create_content_by_scraped_data(array)
    return answer
