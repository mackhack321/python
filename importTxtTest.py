file = open("words.txt","r")
read = file.read()
wlist = {}

with open('words.txt') as file:
    for line in file:
        words = line.split(",")
        for i in words:
            wlist.update({i:"test"})
