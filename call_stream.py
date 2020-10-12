import tweepy
from stream import MyStreamListener


def calling_stream(wordkey, api):
    twitter_listener = MyStreamListener(api, wordkey)
    stream = tweepy.Stream(api.auth, twitter_listener)
    stream.filter(track=[wordkey], languages=["pt"])
