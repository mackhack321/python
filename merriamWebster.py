import json
dictionary = json.load(open("englishdict.json"))

try:
    while True:
        query = input("Word to lookup >>> ")
        try:
            print(dictionary[query.upper()])
        except KeyError:
            print("Word not found")
except KeyboardInterrupt:
    pass
