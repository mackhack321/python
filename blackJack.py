import random as rand
from setsLab import buildDeck, dealHand

deck = buildDeck()

def dealHands():
    phand = dealHand(2,deck=deck)
    chand = dealHand(2,deck=deck)
    return phand,chand

def royalToNum(hand):
    for card in hand:
        if deck[card]["value"].isalpha():
            deck[card]["value"] = "10"
        else: pass

def displayStatus(hand):
    values = [deck[i]["value"] for i in hand]
    return values

hands = dealHands()
print(hands)
playerhand = royalToNum(hands[0])
comphand = royalToNum(hands[1])
print(playerhand, comphand)
