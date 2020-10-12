import tweepy
import logging
import os
from dotenv import load_dotenv

load_dotenv('config.env')
logger = logging.getLogger()


def create_api():
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret_key = os.getenv("CONSUMER_SECRET_KEY")
    acess_token = os.getenv("ACESS_TOKEN")
    acess_secret_token = os.getenv("ACESS_SECRET_TOKEN")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(acess_token, acess_secret_token)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
