import random
import chaosSig
import time

compNum = random.randint(1,20)
guess = -1
amtOfGuesses = 6

name = str.lower(input("new code, who dis?\n"))

print("aye wuss brackin {}? i gotta number between wun and twenny.  guess that dude in 6 or less tries, ya digg?\n".format(name))
#print("aight dogg since you wanna be all debuggy and stuff, the number is {}.".format(compNum))

while guess != compNum and amtOfGuesses != 0:
    try:
        guess = int(input("give it a shot bud\n"))
        if guess < compNum:
            print("naw dogg that too low")
        if guess > compNum:
            print("chill homie, take it down a bit")
        amtOfGuesses = amtOfGuesses - 1
    except ValueError:
        print("cmon dogg.  just gimme a whole number.  no decimals or letters homie.")
        print("imma penalize you two guesses since you gotta act so dumb.\n")
        amtOfGuesses = amtOfGuesses - 2

if amtOfGuesses == 0:
    print("you done run out of chances fool")
    time.sleep(3)
    if name == "Mack":
        print("Error 404: Chaos Not Found")
    else:
        try:
            chaosSig.chaos()
        except KeyboardInterrupt:
            print("Noooo...my only weakness...Ctrl+C...\nX.X")

if guess == compNum:
    print("aight, you hood.  follow me on soundcloud for my new jake paul diss track")
