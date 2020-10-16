import tweepy

from aux_mod import SettStopwords, TransformToCSV
from twitter_data_cleaner import TwitterDataCleaner


class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api, wordkey):
        self.api = api
        self.stopword = SettStopwords(wordkey)
        self.trash = TwitterDataCleaner(self.stopword)

    def on_status(self, tweet):
        is_retweed = hasattr(tweet, "retweeted_status")
        if is_retweed:
            return
        else:
            messy_data = self.trash.clean(tweet.text)
            TransformToCSV(messy_data)

    def on_error(self, status):
        print("Error detected - Stream")
