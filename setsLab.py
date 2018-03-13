class Set:
    def __init__(self, content):
        self.content = content
        self.set = set(content)

    def addElement(self, element):
        self.set.add(element)

    def deleteElement(self, element):
        self.set.discard(element)

    def member(self,element):
        return element in self.set

    def intersection(self, set2):
        return self.set.intersection(set2)

    def union(self, set2):
        return self.set.union(set2)

    def subtract(self, set2):
        return self.set.difference(set2)

class Cards:
    def __init__(self,rank,suit,value):
        self.rank = rank
        self.suit = suit
        self.value = value

def buildDeck():
    cardsfile = open("cards.txt","r")
    contents = cardsfile.readlines()
    counter = 1
    for line in contents:
        while counter < 52:
            rank = line.split("|")[0]
            suit = line.split("|")[1]
            value = line.split("|")[2]
            exec(f"{card}{counter} = Cards(rank,suit,value)")
            counter += 1
