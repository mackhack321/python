from random import randint

print("This is a dice-rolling and coin-flipping simulator.")
quit = "y"
choice = input("Dice or coin? d or c")

if choice == "d":
    input("Press enter to roll the dice.")
    while quit == "y":

        roll = randint(1,6)
        if roll == 1:
            print("You rolled a 1")
        if roll == 2:
            print("You rolled a 2")
        if roll == 3:
            print("You rolled a 3")
        if roll == 4:
            print("You rolled a 4")
        if roll == 5:
            print("You rolled a 5")
        if roll == 6:
            print("You rolled a 6")
        quit = input("Roll again? y or n")
        
if choice == "c":
    input("Press enter to flip a coin.")
    while quit == "y":

        flip = randint(1,2)
        if flip == 1:
            print("Heads")
        if flip == 2:
            print("Tails")
        quit = input("Flip again? y or n")
