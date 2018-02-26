import tweepy
import json
from twitterStream import makeAPI
from twitterJSONLoader import displayFromJSONObject

api = makeAPI("bot")

# statuses = api.user_timeline("Razer")
# jsons = []
# for status in statuses:
#     displayFromJSONObject(status._json)

api.update_status("Hello, world!")
