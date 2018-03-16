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

def dealHand(amt, deck): # takes int for amt and returns hand as a list
    hand = []
    for count in range(1,amt+1):
        randcard = choice(list(deck.keys()))
        hand.append(randcard)
    return hand

def allSame(ls,count):
    sortls = sorted(ls)
    for num in range(0,count+1):
        if sortls[0] == sortls[num]: same = True
        else:
            same = False
            break
    return same

def checkRoyalFlush(ls, suits):
    return "10" in ls and "J" in ls and "Q" in ls and "K" in ls and "A" in ls and allSame(suits, 4)

def checkFullHouse(ls):
    sortls = sorted(ls)
    if sortls[0] == sortls[1] == sortls[2] and sortls[3] == sortls[4]: fullHouse = True
    else: fullHouse = False
    return fullHouse

def isInARow(ls):
    intls = sorted(ls)
    counter = 1
    while counter < len(intls):
        if int(intls[counter]) - int(intls[counter-1]) == 1:
            inRow = True
            counter += 1
        else:
            inRow = False
            break
    return inRow

def checkTwoPairs(ls):
    sortls = sorted(ls)
    if (sortls[0] == sortls[1] and sortls[2] == sortls[3] or
        sortls[1] == sortls[2] and sortls[3] == sortls[4]): twoPairs = True
    else: twoPairs = False
    return twoPairs

def checkPair(ls):
    sortls = sorted(ls)
    if (sortls[0] == sortls[1] or sortls[1] == sortls[2] or
        sortls[2] == sortls[3] or sortls[3] == sortls[4]): pair = True
    else: pair = False
    return pair

def checkHand(hand):
    # Pair – two of same rank (not part of any other hand)
    # X High – If none above fit, X is the highest rank in hand.

    ranks = [deck[i]["rank"] for i in hand]
    suits = [deck[i]["suit"] for i in hand]
    values = [deck[i]["value"] for i in hand]
    ### ROYAL FLUSH ###
    if checkRoyalFlush(values,suits):
        royalFlush = True
    else:
        royalFlush = False

    ### STRAIGHT FLUSH ###
    if allSame(ranks, 4) and allSame(suits, 4): straightFlush = True
    else: straightFlush = False

    ### FOUR OF A KIND ###
    if allSame(ranks, 3): fourKind = True
    else: fourKind = False

    ### FULL HOUSE ###
    if checkFullHouse(ranks): fullHouse = True
    else: fullHouse = False

    ### FLUSH ###
    if allSame(suits, 4): flush = True
    else: flush = False

    ### STRAIGHT ###
    if isInARow(ranks): straight = True
    else: straight = False

    ### THREE OF A KIND ###
    if allSame(ranks, 2) and not allSame(ranks, 3) and not checkFullHouse(ranks): threeKind = True
    else: threeKind = False

    ### TwO PAIRS ###
    if checkTwoPairs(ranks): twoPairs = True
    else: twoPairs = False

    ### PAIR ###
    if checkPair(ranks) and not checkTwoPairs(ranks) and not : pair = True
    else: pair = False

    return {"royalFlush":royalFlush, "straightFlush":straightFlush, "fourKind":fourKind, "fullHouse":fullHouse, "flush":flush,
            "straight":straight, "threeKind":threeKind, "twoPairs":twoPairs, "pair":pair}

if __name__ == "__main__":
    deck = buildDeck()
    handData = {"pair":False}
    while handData["pair"] is False:
        hand = dealHand(amt=5, deck=deck)
        print(hand)
        handData = checkHand(hand)
        print(handData)
