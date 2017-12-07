import math

def pytheorem():
    choice = input("Find hypotenuse or a side? h or s\n")
    if choice == "h":
        a = float(input("A?\n"))
        b = float(input("B?\n"))
        c = float(math.sqrt(a**2+b**2))
        print("The hypotenuse is "+str(c)+" units.")
    if choice == "s":
        a = float(input("Give the length of one leg.\n"))
        c = float(input("Give the hypotenuse.\n"))
        b = float(math.sqrt(c**2-a**2))
        print("The length of the unknown leg is "+str(b)+" units.")

def midpointForm():
    xOne = float(input("Give the X value of the first point.\n"))
    yOne = float(input("Give the Y value of the first point.\n"))
    xTwo = float(input("Give the X value of the second point.\n"))
    yTwo = float(input("Give the Y value of the second point.\n"))

    midx,midy = (xOne+xTwo)/2, (yOne+yTwo)/2
    print("The midpoint is ("+str(midx)+", "+str(midy)+").")

def distanceForm():
    xOne = float(input("Give the X value of the first point.\n"))
    yOne = float(input("Give the Y value of the first point.\n"))
    xTwo = float(input("Give the X value of the second point.\n"))
    yTwo = float(input("Give the Y value of the second point.\n"))

    dist = float(math.sqrt((xTwo-xOne)**2+(yTwo-yOne)**2))
    print("The distance between the two given points is "+str(dist)+" units.")

def improperToMixed():
    num = int(input("Give the numerator of the improper fraction."))
    den = int(input("Give the denominator of the improper fraction."))

    newNum = num // den
    newDen = num % den
    print("The mixed number is {} and {}/{}".format(newNum,newDen,den))

def mixedToImproper():
    wholeNum = int(input("Give the whole number."))
    num = int(input("Give the numerator of the fraction."))
    den = int(input("Give the denominator of the fraction."))

    newNum = den*wholeNum+num
    print("The improper fraction is {}/{}.".format(newNum,den))

def slopeFinder():
    xOne = float(input("Give the X value of the first point.\n"))
    yOne = float(input("Give the Y value of the first point.\n"))
    xTwo = float(input("Give the X value of the second point.\n"))
    yTwo = float(input("Give the Y value of the second point.\n"))
    
    try:
        slope = (yTwo-yOne)/(xTwo-xOne)
        print("The slope of the line that passes through the given points is {}.".format(slope))
    except ZeroDivisionError:
        print("Cannot divide by zero.  Undefined slope!")

def tempConv():
    choice = input("F to C or C to F? fc or cf\n")
    if choice == "cf":
        cel = float(input("Give the measurement in Celcius.\n"))
        fah = float(cel*9/5+32)
        print("{} degrees Celcius is {} degrees Fahrenheit.".format(cel,fah))
    if choice == "fc":
        fah = float(input("Give the measurement in Fahrenheit.\n"))
        cel = (fah-32)/(9/5)
        print("{} degrees Fahrenheir is {} degrees Celcius.".format(fah,cel))      

def unitToInches():
    unit = input("Convert millimeters or centimeters to inches? m or c\n")
    amt = float(input("Give the measurement.\n"))
    if unit == "m":
        inch = float((1/25.4)*amt)
        print("{} millimeters is {} inches.".format(amt,inch))
    if unit == "c":
        inch = float((1/2.54)*amt)
        print("{} centimeters is {} inches.".format(amt,inch))

def fracSimp():
    try:
        num = int(input("Input the numerator of the fraction to simplify.\n"))
        den = int(input("Input the denominator of the fraction to simplify.\n"))
        gcd = math.gcd(num,den)
        
        newNum = int(num/gcd)
        newDen = int(den/gcd)
        print("{}/{} simplified is {}/{}.".format(num,den,newNum,newDen))
        
    except ValueError:
        print("Decimal values cannot be the numerator or denominator of a fraction.")

def quadForm():
    a = int(input("A?"))
    b = int(input("B?"))
    c = int(input("C?"))

    try:
        ansPlus = (-b+math.sqrt(b**2-4*a*c))/2*a
        ansMin = (-b-math.sqrt(b**2-4*a*c))/2*a
        print("The answer is {} or {}.".format(ansPlus,ansMin))
    except ValueError:
        print("Value Error: No Real Solution!")

print("This program is Certified Non-Chaotic.\n")
print("Pythagorean Theorem - 1\nMidpoint Formula - 2\nDistance Formula - 3")
print("Improper to Mixed - 4\nMixed to Improper - 5\nSlope Finder - 6")
print("Temperature Conversion - 7\nCenti/Millimeters to Inches - 8\nFraction Simplifier - 9")
print("Quadratic Formula - 0\n")
choice = input("Give the number assigned to the subject of your choice.\n")

if choice == "1":
    pytheorem()
elif choice == "2":
    midpointForm()
elif choice == "3":
    distanceForm()
elif choice == "4":
    improperToMixed()
elif choice == "5":
    mixedToImproper()
elif choice == "6":
    slopeFinder()
elif choice == "7":
    tempConv()
elif choice == "8":
    unitToInches()
elif choice == "9":
    fracSimp()
elif choice == "0":
    quadForm()
else:
    print("{} is not a valid option.".format(choice))
