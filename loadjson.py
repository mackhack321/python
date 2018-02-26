import json
jsonfile = open("streamdata.json","r")
contents = jsonfile.read()
data = contents.split("\n\n")[0]
jsondata = json.loads(data)

user = jsondata["user"]["screen_name"]
tweet = jsondata["text"]
date = jsondata["created_at"]
print(f"On {date}, user {user} tweeted :: {tweet}")
