from random import *

def dice():
    check = False
    while check != "y" and check != "n":
        check = str.lower(input("Roll? y or n: "))
        if check == "y":
            again = True
            while again is True:
                colors = ["Pink","Yellow","Brick Red","Chartreuse","Maroon","Purple"]
                randNum = randint(1,6)
                randColor = choice(colors)
                print(f"You rolled a {randNum} and a {randColor}!")

                again = "bob"
                while again != "y" and again != "n":
                    again = str.lower(input("Again? y or n: "))
                if again == "y":
                    again = True
                    continue
                elif again == "n":
                    again = False
                    break
        if check == "n":
            break
    print("Goodbye!")

dice()
