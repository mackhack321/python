# This is a guess the number game.
import time
import random
import chaosSig
guessesTaken = 0

myName = input('Hello! What is your name?')
number = random.randint(1, 20)
if myName == "Mack":
    print('Greetings, my Lord. I am thinking of a number between 1 and 20.')
else:
    print("Well, "+ myName +", I'm thinking of a number between 1 and 20.")

while guessesTaken < 6: 

    guess = input('Take a guess.')
    guess = int(guess)
    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low.')
    if guess > number:
        print('Your guess is too high.')
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number +".  Now, prepare for the wrath of a seemingly endless stream of numbers.")
    
    time.sleep(5)
    chaosSig.chaos()
