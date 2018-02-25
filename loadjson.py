def jsonToDict(filename):
    with open(f"{filename}") as jsondata:
        data = json.load(jsondata)
        jsondata.close
    return data

import json
data = jsonToDict(filename = "razer.json")
print(data["created_at"])
print(data["text"])

