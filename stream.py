import tweepy
import os
from dotenv import load_dotenv

from to_csv import TransformToCSV
from twitter_data_cleaner import TwitterDataCleaner

load_dotenv("wordkey.env")

def calling_stream(api: tweepy):
    twitter_listener = MyStreamListener(api)
    stream = tweepy.Stream(api.auth, twitter_listener)
    stream.filter(track=[os.getenv("WORDKEY")], languages=["pt"])

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api

    def on_status(self, tweet):
        is_retweed = hasattr(tweet, "retweeted_status")
        if is_retweed:
            return
        else:
            messy_data = TwitterDataCleaner(tweet.text)
            TransformToCSV(messy_data)

    def on_error(self, status):
        print("Error detected - Stream")
