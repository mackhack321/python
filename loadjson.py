import json
def displayFromJSONObject(jsonobject):
    user = jsonobject["user"]["screen_name"]
    tweet = jsonobject["text"]
    date = jsonobject["created_at"]
    print(f"On {date}, user {user} tweeted :: {tweet}")

def __main__():
    jsonfile = open("streamdata.json","r")
    contents = jsonfile.read().split("\n\n")
    for tweetdata in contents:
        try:
            jsonobject = json.loads(tweetdata)
            displayFromJSONObject(jsonobject)
        except json.decoder.JSONDecodeError:
            pass

if __name__ == "__main__":
    __main__()
