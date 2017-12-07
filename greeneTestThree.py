from time import *
def gradecomp():
    valid = False
    while valid is False:
        #gimme those sweet, sweet bonus points
        try:
            #I am painfully aware of the fact that round() won't round a float up if it ends in .5, but this
            #is as close as it's gonna get.  Turning the input into a float allows for decimal grades
            numgrade = round(float(input("Enter a numerical score, omit the percent sign: ")), 0)
            valid = True
        except ValueError:
            print("Invalid grade.  Did you omit the percent sign?")
    if numgrade < 0:
        strgrade = "Z.  How did you manage to pull this off?"
    elif numgrade > 90:
        strgrade = "A"
    elif numgrade > 80:
        strgrade = "B"
    elif numgrade > 70:
        strgrade = "C"
    elif numgrade > 60:
        strgrade = "D"
    elif numgrade <= 60:
        strgrade = "F.  F for failure.  You should feel bad for yourself."
    print("You have earned the letter grade: {}".format(strgrade))
    sleep(2)
    print()

def numavg():
    ls = []
    finished = False
    while finished is False:
        num = input("Give a number or say 'finished': ")
        if num.lower() == "finished":
            finished = True
            numsum = sum(ls)
            try:
                avg = numsum/len(ls)
            except ZeroDivisionError:
                print("You have given no grades to be averaged")
                finished = False
                continue
            print("Count: {}".format(len(ls)))
            print("Sum: {}".format(numsum))
            print("The average of the given numbers is: {}".format(avg))
            break
        try:
            num = float(num)
            ls.append(num)
            print("Numbers in list so far: {}".format(ls))
        except ValueError:
            print("Invalid number!")
            continue
    sleep(2)
    print()

print("Hello there.  This Mack's second test sumission.")
print("This one actually follows ALL of the directions.\n")
valid = False
while valid is False:
    print("Grade Program - 1")
    print("Number Averager - 2")
    print("Exit Launcher - 3\n")
    choice = input("Pick a program to run: ")
    if choice == "1":
        valid = True
        print()
        gradecomp()
        valid = False
    elif choice == "2":
        valid = True
        print()
        numavg()
        valid = False
    elif choice == "3":
        print("Goodbye")
        break
    else:
        print("Invalid choice.")
