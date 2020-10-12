import tweepy
from twitter_data_cleaner import TwitterDataCleaner

# authorization tokens
consumer_key = "cjCljFRvCXdvEwd53KzQA6myi"
consumer_secret = "pKnK7GdtOzi1HFlxmetLqy4Oe6nWtMzSwQIy5AHTgFEf1UaS1Z"
access_key = "1283256710031912961-Ekp0uKwnKp9616Uu0nhwtO94AEywWK"
access_secret = "P36lXRzUxQhMAeH7vSntQCPfVaZjekMlsVXdtdL6RsdJy"


class StreamListener(tweepy.StreamListener):

    def __init__(self, api, stopword):
        self.api = api
        self.stopword = stopword
        self.trash = TwitterDataCleaner(stopword)

    def on_status(self, status):
        is_retweet = hasattr(status, "retweeted_status")
        if is_retweet:
            return
        print(self.trash.clean(status.text))

    def on_error(self, status_code):
        print("Encountered streaming error (", status_code, ")")


# complete authorization and initialize API endpoint
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# initialize stream
streamListener = StreamListener(api, 'corona')
stream = tweepy.Stream(auth=api.auth, listener=streamListener)
stream.filter(track='corona')
