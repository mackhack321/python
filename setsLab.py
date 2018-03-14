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

def allSame(ls):
    for item in ls:
        if ls[0] == item: same = True
        else:
            same = False
            break
    return same

def checkHand(hand):
    # Royal flush – 10, Jack, Queen, King, Ace all same suit
    # Straight flush – five ranks in a row, all same suit
    # Four of a kind – Four of same rank
    # Full house – three of one rank and two of another
    # Flush – five of same suit
    # Straight – five ranks in row
    # Three of a kind – three of one rank (not part of four or full house)
    # Two pair – two each of two ranks
    # Pair – two of same rank (not part of any other hand)
    # X High – If none above fit, X is the highest rank in hand.
    ranks = [deck[i]["rank"] for i in hand]
    suits = [deck[i]["suit"] for i in hand]
    values = [deck[i]["value"] for i in hand]
    if "10" in values and "J" in values and "Q" in values and "K" in values and "A" in values and allSame(suits):
        royalFlush = True

deck = buildDeck()
hand = dealHand(amt=5)
print(hand)
checkHand(hand)
