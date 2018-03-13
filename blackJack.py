import random
def Main():
    A = 0
    houseSum = 0
    cardNum = []
    cardDrawn = []
    deck = {1:"Ace of Spades", 2:"2 of Spades", 3:"3 of Spades", 4:"4 of Spades", 5:"5 of Spades", 6:"6 of Spades",
    7:"7 of Spades", 8:"8 of Spades", 9:"9 of Spades", 10:"10 of Spades", 11:"Jack of Spades", 12:"Queen of Spades", 13:"King of Spades",
    14:"Ace of Spades", 15:"2 of Spades", 16:"3 of Spades", 17:"4 of Spades", 18:"5 of Spades", 19:"6 of Spades",
    20:"7 of Spades", 21:"8 of Spades", 22:"9 of Spades", 23:"10 of Spades", 24:"Jack of Spades", 25:"Queen of Spades", 26:"King of Spades",
    27:"Ace of Hearts", 28:"2 of Hearts", 29:"3 of Hearts", 30:"4 of Hearts", 31:"5 of Hearts", 32:"6 of Hearts",
    33:"7 of Hearts", 34:"8 of Hearts", 35:"9 of Hearts", 36:"10 of Hearts", 37:"Jack of Hearts", 38:"Queen of Hearts", 39:"King of Hearts",
    40:"Ace of Diamonds", 41:"2 of Diamonds", 42:"3 of Diamonds", 43:"4 of Diamonds", 44:"5 of Diamonds", 45:"6 of Diamonds",
    46:"7 of Diamonds", 47:"8 of Diamonds", 48:"9 of Diamonds", 49:"10 of Diamonds", 50:"Jack of Diamonds", 51:"Queen of Diamonds", 52:"King of Diamonds"}
    while A < 2:
        card = random.randint(1,52)
        cardDrawn.append(deck[card])
        #print("Beep")  # Troubleshooting
        if card >= 14 and card <= 26:
            cardNum.append(card - 13)
        elif card >= 27 and card <= 39:
            cardNum.append(card - 26)
        elif card >= 40:
            cardNum.append(card - 39)
        else:
            cardNum.append(card)
        A += 1

        houseFirst = random.randint(1,52)
        houseCard1 = deck[houseFirst]
        if houseFirst >= 14 and houseFirst <= 26:
            houseFirst -= 13
        elif houseFirst >= 27 and houseFirst <= 39:
            houseFirst -= 26
        elif houseFirst >= 40:
            houseFirst -= 39
        houseSecond = random.randint(1,52)
        houseCard2 = deck[houseSecond]
        if houseSecond >= 14 and houseSecond <= 26:
            houseSecond -= 13
        elif houseSecond >= 27 and houseSecond <= 39:
            houseSecond -= 26
        elif houseSecond >= 40:
            houseSecond -= 39
        houseSum = (houseFirst + houseSecond)
        if houseSum > 21:
            houseFirst = 0
            houseFirst = random.randint(1,52)
            houseCard1 = deck[houseFirst]
            if houseFirst >= 14 and houseFirst <= 26:
                houseFirst -= 13
            elif houseFirst >= 27 and houseFirst <= 39:
                houseFirst -= 26
            elif houseFirst >= 40:
                houseFirst -= 39
            houseSecond = 0
            houseSecond = random.randint(1,52)
            houseCard2 = deck[houseSecond]
            if houseSecond >= 14 and houseSecond <= 26:
                houseSecond -= 13
            elif houseSecond >= 27 and houseSecond <= 39:
                houseSecond -= 26
            elif houseSecond >= 40:
                houseSecond -= 39
            houseSum = (houseFirst + houseSecond)

    cardSum = sum(cardNum)
    print("Your cards are as follows:", ", ".join(cardDrawn), f"for a total of {cardSum},")
    print(f"The house got {houseCard1},", f"or {houseFirst}.\n")
    while cardSum < 21:
        try:
            hitOrCheck = int(input("Would you like to hit(1) or check(2)? \n"))
            if hitOrCheck == 1:
                card = random.randint(1,52)
                cardDrawn.append(deck[card])
                #print("Beep")  # Troubleshooting
                if card >= 14 and card <= 26:
                    cardNum.append(card - 13)
                elif card >= 27 and card <= 39:
                    cardNum.append(card - 26)
                elif card >= 40:
                    cardNum.append(card - 39)
                else:
                    cardNum.append(card)
                cardSum = sum(cardNum)
                print("Your cards are as follows:", " and the ".join(cardDrawn), f"for a total of {cardSum}.\n")
            elif hitOrCheck == 2:
                break
        except:
            print("Use either a 1 or a 2 corresponding to your choice.\n")

    if cardSum == 21 and cardSum > houseSum:
        print(f"Congradulations. You got a 21, but the house had {houseSum}.")
    elif cardSum <= 21 and cardSum > houseSum:
        print(f"You beat the house with a total of {cardSum}, whereas the house got {houseSum}.")
    elif cardSum <= 21 and cardSum < houseSum:
        print(f"The house beat you with a total of {houseSum}.")
    else:
        print(f"Whoops. You busted, and the house wins with a {houseSum}.")

Main()
