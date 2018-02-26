import tweepy
import json
from twitterJSONLoader import displayFromJSONObject

def makeAPI(account):
    ### AUTHORIZE AND INITIATE API SESSION ###
    if account == "real":
        consumer_key = "zof0VBLnjHn4Y5bWtd6u1r607"
        consumer_secret = "qF1A1QxBjTBKEsQbk1RPoW5taRKaX5rirvHAz79L5ma2pwIwJr"
        access_key = "2605988078-3xOp3rx7BF6e4jjXXd490AqbcSD1FdIuAKHsVgn"
        access_secret = "wKIRrGo7EvwRdYoeEt7r87Id4CmHvNlCh2UjBezCo00wi"

    if account == "bot":
        consumer_key = "lObKvENEwohkGcxt685W184VW"
        consumer_secret = "CnN2Kl96OTXCc3s4i5drwVZZgb5q3q3zoM1RKMXl5llJvPNKQh"
        access_key = "968148646393982976-Ei5UgZ2dUAVBFkPvqw455zX4gnHSHbn"
        access_secret = "YbNgJoK6Dg4vrISgw8vTbHesW2syhOMrQN6PMncdo3Bf0"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    return api
    ##########################################

def writeToJSON(listOfJSONs, filename):
    jsonfile = open(filename,"a")
    print(f"Writing objects to {filename}...")
    for obj in listOfJSONs:
        json.dump(obj, jsonfile, indent = 4, sort_keys = True)
        jsonfile.write("\n\n")
    jsonfile.close()
    print(f"Done!  Wrote {len(listOfJSONs)} objects to {filename}")

class MyStreamListener(tweepy.StreamListener):
    def on_data(self, data):
        while len(tweets) < 50: # set number to how many tweets you want to grab
            tweets.append(json.loads(data))
            try:
                displayFromJSONObject(json.loads(data))
            except: # removes non-tweet objects found in data
                tweets.remove(json.loads(data))
            return True
        return False

    def on_error(self,status_code):
        if status_code == 420:
            print("Error 420 caught, killing stream...")
            return False

def __main__():
    global tweets # this list needs to be visible to everyone
    tweets = [] # will hold json objects
    api = makeAPI("real") # get api session from func defined above
    myStream = tweepy.Stream(auth = api.auth, listener = MyStreamListener())
    myStream.filter(track = ["school shooting"]) # define search keyword
    writeToFile = True # write to file? True or False
    if writeToFile is True:
        writeToJSON(tweets, "streamdata.json") # change second arg to desired filename, including ext

if __name__ == "__main__":
    __main__()
