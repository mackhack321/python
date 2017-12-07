import random
import time
import chaosSig
#cheat codes:
#sword (rand chance that you'll kill the dragon if it tries to eat you)
#dig (secret third cave, but is actually chaos)
#hack.exe (homage to finch, always get good cave)
#tam (self explanatory)
#wilson (roast overlord)
def intro():
    print("The date is 443X.  You are a traveler, traversing the vast lands of Icelandia(TM).")
    time.sleep(2)
    print("You stumble across a small village with few inhabitants.")
    time.sleep(2)
    print("You see an old man with a large beard.  You assume that this man is incredibly wise due to the girth of his beard.  You approach the man.")
    time.sleep(2)
    print("The man tells you of two caves that are located in the heart of the village.")
    time.sleep(2)
    print("He tells you that in the heart of each cave, there lies a mighty dragon.")
    time.sleep(2)
    print("One of the dragons, he says, is kind and will share his treasure with you.")
    time.sleep(2)
    print("However, he describes the second dragon as a man-eating freak of nature.")
    time.sleep(2)

def chooseCave():
    print("After walking for a few hours, you reach the heart of the village and approach the two caves.")
    time.sleep(2)
    chosenCave = ''
    code = "null"
    while chosenCave != "1" and chosenCave != "2":
        print("It's time to make a decision.  Which cave will you enter? 1 or 2")
        chosenCave = input()
        if chosenCave == "cheat":
            code = input("Enter your cheat code, you scum...\n")
            print("Code \"{}\" activated.  It might do stuff, it might not.".format(code))

    if code == "hack.exe":
        print("You feel the presense and blessings of the spirit of another Creator...")
        time.sleep(2)
    print("You walk into the cave and go deeper until you reach the heart of the cave.")
    time.sleep(2)
    print("You come across the dragon the wise man spoke of.")
    time.sleep(2)
    print("The dragon stares at you intently and...")
    time.sleep(3)

    if code == "hack.exe":
        goodCave = chosenCave
    else:
        goodCave = str(random.randint(1,2))
    #goodCave = "1" #uncomment to force 1 as good cave
    if code == "dig":
        print("Shortly after you make your decision, you decide against following directions like the deviant hero you are.")
        time.sleep(2)
        print("You pull out a shovel you found earlier in the village and dig into the soft ground under you...")
        time.sleep(2)
        print("...and you come across a third cave!")
        time.sleep(2)
        print("You drop into the cave and find a sign that reads...")
        time.sleep(2)
        print("\"Cheaters never prosper, unless you're in one of the Great Creator's creations...")
        print("...And you are.  But some codes are bound to be duds.  Chaos inbound!\"")
        time.sleep(5)
        try:
            chaosSig.chaos()
        except KeyboardInterrupt:
            print("\nTry again soon, \"hero.\"")
    elif chosenCave == goodCave:
        print("...shares some of his treasure with you!")
        time.sleep(2)
        print("You return to the village and share some of your sweet loot.  A true hero you are.")
        if code == "tam":
            time.sleep(2)
            print("...but your battle isn't over yet, hero.")
            time.sleep(2)
            print("Tam approaches.")
            time.sleep(2)
            print("You are paralyzed by the sheer power of her being.")
            time.sleep(2)
            print("You snap out of it after a few seconds, and you enter fight or flight mode.")
            time.sleep(2)
            print("You have a 50/50 chance of winning this battle.  Either you do, or you don't.")
            time.sleep(2)
            choice = "null"
            while choice != "b":
                choice = input("Will you strike, flee, or bow down? s, f, or b\n")
                if choice == "s":
                    print("Your petty attempt at striking Tam was shot down by her defensive maneuvers learned from CPI training.")
                elif choice == "f":
                    print("There is no escaping the wrath of Tam.")
                elif choice == "b":
                    print("The teachings of Tam consume you.  You have become Ascended.")
        elif code == "wilson":
            time.sleep(2)
            print("...but your battle isn't over yet, hero.")
            time.sleep(2)
            print("Mr. Wilson, roast overlord, approaches.")
            time.sleep(2)
            print("You are paralyzed by the amount of potential roast energy.")
            time.sleep(2)
            print("You snap out of it after a few seconds, and you enter fight or flight mode.")
            time.sleep(2)
            print("Mr. Wilson becomes Ascended.")
            time.sleep(2)
            choice = "null"
            while choice != "b":
                choice = input("Will you strike, flee, or bow down? s, f, or b\n")
                if choice == "s":
                    print("Mr. Wilson summons a phospholipid bilayer that protects him from any attack.")
                elif choice == "f":
                    print("As you try to flee, Mr. Wilson denatures the proteins in your body.  Your chromosomes are reworked and you now have a number of genetic disorders.")
                elif choice == "b":
                    print("You are spared by Mr. Wilson.  You surrender yourself to his power.")
                    time.sleep(2)
                    print("You were once as lost as last year's easter egg, but now you are found.")
    else:
        print("...gobbles you up with one bite!  You've become the dragon's brunch.")
        time.sleep(2)
        if code == "sword":
            swordRand = str(random.randint(1,2))
            if swordRand == "1":
                print("...but wait!  Using the sword you got from the cheat code, you sliced open the dragon's digestive tract!")
                time.sleep(2)
                print("You return to the village and share some of your sweet loot.  A true hero you are.")            
            else:
                print("The whole village mourns your death.  You were supposed to be their hero.  What a disappointment you are.")
        else:
            print("The whole village mourns your death.  You were supposed to be their hero.  What a disappointment you are.")

again = "y"
while again == "y":
    intro()
    chooseCave()
    again = input("Play again? y or n\n")
else:
    print("Farewell, hero.")
