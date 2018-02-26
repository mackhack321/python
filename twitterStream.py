import tweepy
import json

consumer_key = "zof0VBLnjHn4Y5bWtd6u1r607"
consumer_secret = "qF1A1QxBjTBKEsQbk1RPoW5taRKaX5rirvHAz79L5ma2pwIwJr"
access_key = "2605988078-3xOp3rx7BF6e4jjXXd490AqbcSD1FdIuAKHsVgn"
access_secret = "wKIRrGo7EvwRdYoeEt7r87Id4CmHvNlCh2UjBezCo00wi"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):
    def on_data(self, data):
        #data = data.split('"text":')[1].split(',"source"')[0]
        while len(tweets) < 5:
            tweets.append(json.loads(data))
            print(json.loads(data))
            return True
        return False
    def on_status(self, status):
        print(status.text)
    def on_error(self,status_code):
        if status_code == 420:
            print("Error 420 caught, killing stream...")
            return False

tweets = []
jsonfile = open("streamdata.json","a")
myStream = tweepy.Stream(auth = api.auth, listener = MyStreamListener())
myStream.filter(track = ["fortnite"])

for tweet in tweets:
    json.dump(tweet,jsonfile, indent = 4, sort_keys = True)
    jsonfile.write("\n\n")
