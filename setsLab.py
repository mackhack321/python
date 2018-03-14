from random import choice
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

def buildDeck(): # returns dict
    cardfile = open("cards.txt","r")
    lines = cardfile.readlines()
    cardfile.close()
    deck = {}
    for line in lines:
        rank = line.split("|")[0].replace("\n","")
        suit = line.split("|")[1].replace("\n","")
        value = line.split("|")[2].replace("\n","")
        deck.update({f"{value}{suit}":{"rank":rank, "value":value, "suit":suit}})
    return deck

def dealHand(amt): # takes int for amt and returns hand as a list
    hand = []
    for count in range(1,amt+1):
        randcard = choice(list(deck.keys()))
        hand.append(randcard)
    return hand

def checkHand(hand):
    ranks = [deck[i]["rank"] for i in hand]
    suits = [deck[i]["suit"] for i in hand]
    value = [deck[i]["value"] for i in hand]
    print(ranks,suits,value)

deck = buildDeck()
hand = dealHand(amt=5)
print(hand)
checkHand(hand)
