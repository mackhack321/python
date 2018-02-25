def jsonToDict(filename):
    with open(f"{filename}") as jsondata:
        data = json.load(jsondata)
        jsondata.close
    return data

import json
data = jsonToDict(filename = "mack.json")
data = data["people"]

for entry in data:
    name = entry["name"]
    age = entry["age"]
    print(f"{name} is {age} years old")
