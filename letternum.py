from string import ascii_uppercase
from random import choice

def buildDict(): # build dictionary where key=letter and val=number in alphabet
    letters = {}
    counter = 1
    for letter in ascii_uppercase:
        letters[letter] = counter
        counter += 1
    return letters

def isWord(word):
    return word.lower() in engdict

def checkword(word):
    return sum([letters[i] for i in word])

def getword():
    vals = []
    word = []
    while sum(vals) != 100 and not done:
        if sum(vals) > 100: word = []; vals = []
        randletter = choice(list(letters.keys()))
        word.append(randletter)
        vals.append(letters[randletter])
    return "".join(word)

letters = buildDict()

with open("dict.txt","r") as f:
    engdict = f.readlines()
    f.close()

done = False
while not done:
    word = getword()
    print(word)
    done = isWord(word)
