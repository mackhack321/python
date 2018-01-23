try:
    import math
except ImportError:
    print("Your machine does not have the Python math library installed.")
    print("This program is not compatiable with your machine.")

def exponent():
    print("I'm a filler function!  TEMPNAME ran.")
    print("This program raises X to the power of Y.")
    try:
        x = int(input("Give X: "))
        y = int(input("Give Y: "))
    except ValueError:
        print("Invalid formatting of variables")
        input("Press enter to restart...")
        exponent()
    try:
        print(f"{x} to the power of {y} is {math.pow(x,y)}.")
    except OverflowError:
        print("Numbers as big as that make my brain hurt... :(")
        input("Press enter to restart...")
        exponent()
    input("Press enter to return to the launcher...")

def TEMPNAME2():
    print("I'm a filler function!  TEMPNAME2 ran.")

def TEMPNAME3():
    print("I'm a filler function!  TEMPNAME3 ran.")

def about():
    print("This program is meant to demonstrate the use of functions")
    print("and the basics of a user interface.  Each function holds")
    print("its own mathematical function, allowing for easy ")
    print("troubleshooting and readability (in theory).")
    input("Press enter to return to the launcher...")

def launcher():
    print("=====Launcher=====")
    print("1 --- Raise X to Y")
    print("2 ------ TEMPNAME2")
    print("3 ------ TEMPNAME3")
    print("4 ---------- About")
    print("5 ----------- EXIT")
    print("==================")
    choice = input("Enter the number of your choice: ")
    if choice == "1":
        exponent()
        launcher()
    elif choice == "2":
        TEMPNAME2()
        launcher()
    elif choice == "3":
        TEMPNAME3()
        launcher()
    elif choice == "4":
        about()
        launcher()
    elif choice == "5":
        pass
    else:
        launcher()

launcher()
