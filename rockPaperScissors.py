#Rock Paper Scissors
import random
import time
from chaosSig import chaos

name = input("What's your name?\n")
if name == "Mack":
    print("Greetings, my Great Creator.  You know what to do.")
    print("---Chaos has been disabled!---")
else:
    print("Hey, "+name+".  I'm another one of the Great Creator's creations.  Let's play Rock, Paper, Scissors.  You must win 3 times in 10 or less tries.\n")

aiOptions = ["rock","paper","scissors"]

wins = 0
tries = 0

while wins != 3:
    choice = input("Rock, paper, or scissors? The computer can't see your choice. r, p, or s\n")

    aichoice = random.choice(aiOptions)
    
    if choice == "r" and aichoice == "rock":
        print("It's a draw!")
    if choice == "r" and aichoice == "paper":
        print("You lose! The computer chose "+aichoice+".")
    if choice == "r" and aichoice == "scissors":
        print("You win!")
        wins = wins + 1

    if choice == "p" and aichoice == "rock":
        print("You win!")
        wins = wins + 1
    if choice == "p" and aichoice == "paper":
        print("It's a draw!")
    if choice == "p" and aichoice == "scissors":
        print("You lose! The computer chose "+aichoice+".")
        
    if choice == "s" and aichoice == "rock":
        print("You lose! The computer chose "+aichoice+".")
    if choice == "s" and aichoice == "paper":
        print("You win!")
        wins = wins + 1
    if choice == "s" and aichoice == "scissors":
        print("It's a draw!")

    tries = tries + 1

print("Congrats, you won. It took you "+str(tries)+" tries...")
if tries >= 10:
    print("...and that's a bit too many.  Prepare for utter chaos.")
    time.sleep(3)
    if name == "Mack":
        print("Error 404: Chaos not found.  (Chaos is disabled under your name, my Great Creator.)")
    else:
        chaos()
else:
    print("...and that's just the right amount! Good job.")
