#A program that asks for items, puts them in a list, and then randomly selects one item from that list.
import random
options = []

more = "y"

def addToList():
    ask = input("Give an option to add to the list of possibilities. (min. of 2)\n")
    options.append(ask)
    
addToList()

while more == "y":
    addToList()
    more = input("Add another option? y or n\n")
else:
    
    def choose():
        print("Your list:", options)
        print("The item that was randomly selected is:")
        print(random.choice(options))
    choose()
    
    again = input("Pick another item? y or n\n")
    
    while again == "y":
        choose()
        again = input("Pick another item? y or n\n")
