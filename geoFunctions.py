import math

def areaOfCircle():
    try:
        rad = float(input("Give the radius of the circle: "))
    except ValueError:
        input("Invalid input.  Press enter to restart...")
        areaOfCircle()
    area = math.pi*(rad**2)
    print(f"The area of a circle with a radius of {rad} is {area}.")
    input("Press enter to return to the launcher...")

def areaOfRec():
    try:
        l = float(input("Give the length of the rectangle: "))
        w = float(input("Give the width of the rectangle: "))
    except ValueError:
        print("Invalid input.  Press enter to restart...")
        areaOfRec()
    area = l*w
    print(f"The area of a rectangle with a length of {l} and a width of {w} is {area}.")
    input("Press enter to return to the launcher...")

def circumOfCircle():
    try:
        rad = float(input("Give the radius of the circle: "))
    except ValueError:
        input("Invalid input.  Press enter to restart...")
        circumOfCircle()
    circum = 2*math.pi*rad
    print(f"The circumference of a circle with a radius of {rad} is {circum}")
    input("Press enter to return to the launcher...")

def about():
    print("This program is meant to demonstrate the use of functions")
    print("and the basics of a user interface.  Each function holds")
    print("its own mathematical function, allowing for easy ")
    print("troubleshooting and readability (in theory).")
    input("Press enter to return to the launcher...")
