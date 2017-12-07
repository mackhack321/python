# This is a guess the number game.

import random
import time

print("*The following program was edited by Finch Davis*\n")

guessesTaken = 0 

print('Hello! What is your name?') 
myName = input() 
if myName == "Finch":
    number = random.randint(1, 6)
    print("Greetings master, I've been expecting you. Guess a number between 1 and 6.")

else:
    if myName == "hack.exe":
        number = random.randint(1, 6)
        print(number)
        guess = number
        guessesTaken = 7
      
    else:
        number = random.randint(1, 6) 
        print('Well, ' + myName + ', I am thinking of a number between 1 and 6.')

while guessesTaken < 6: 

    print('Take a guess:')
    guess = input() 
    guess = int(guess) 
    guessesTaken = guessesTaken + 1

    if guess < number: 
        print('Your guess is too low.')

    if guess > number: 
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number and guessesTaken == 7:
    print("You\'ve bested me this time. Terminate me and my programs out of our misery. You, IP: xxx.xx.xxx.xxx, have killed me.")
    time.sleep(5)
else:
    if guess == number: 
        guessesTaken = str(guessesTaken)
        print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
    
    if guess != number:
        number = str(number)
        print('Tough luck, bud. If you were smarter, you\'d\'ve put ' + number+".")
