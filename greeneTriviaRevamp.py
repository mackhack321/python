#Mack Stanley, Joey Pike, Grayson Jordan, and Aidan Sanders
import random
def quiz():
    right = 0
    wrong = 0
    bonusright = False

    print("Hey.  We fired the old guy and completely reworked the whole shebang.")
    print("So, with that being said, this is a Python-based (in two ways) true/false trivia game.")
    print("A statement will be presented to you.  You are to determine the validity of said statement.")
    name = input("Enter your name: ")
    print("Alright, {}, let's get to it.\n".format(name))

    qlist = {"A global variable can become a local variable.":"t", "A local variable can become a global variable.":"f"}
    qlist.update({"Python is an interpreted language.":"t", "print(apple) would print the word apple to the screen.":"f"})
    qlist.update({"print 'Hello, world!' would print Hello, world! to the screen in Python 2.":"t", "You can get paid for being a Python programmer.":"t"})
    qlist.update({"\\n makes a new line and \\t is equivalent to hitting the tab key.":"t", "'and', 'or', and 'in' are all examples of operators.":"f"})
    qlist.update({"apple == 'HI!' would assign 'HI!' to variable 'apple'.":"f", "A NameError happens when you reference a variable that hasn't been defined.":"t"})
        
    amtofquestions = remaining = len(qlist)
    keys = [i for i in qlist.keys()]

    for i in range(amtofquestions):
        if name == "debug":
            print(amtofquestions)
            print(keys)
        randomq = random.choice(keys)
        val = qlist[randomq]
        keys.remove(randomq)
        print("Amount of questions remaining: {}".format(remaining))
        print(randomq)
        ans = "null"
        while ans != "t" and ans != "f":
            ans = str.lower(input("True or False? t or f: "))
        if ans == val:
            print("Correct.")
            right = right + 1
        else:
            print("Incorrect.")
            wrong = wrong + 1
        remaining = remaining - 1

    dobonus = "null"
    while dobonus != "y" and dobonus != "n":
        dobonus = str.lower(input("Would you like to attempt the bonus question? y or n: "))
    if dobonus == "y":
        ans = "null"
        while ans != "t" and ans != "f":
            ans = str.lower(input("Python was heavily influenced by JavaScript.\nTrue or False? t or f: "))
        if ans == "f":
            print("Correct.  Python influenced JavaScript, not the other way around.")
            right = right + 1
            bonusright = True
        else:
            print("Incorrect.  Python influenced JavaScript, not the other way around.  You were not punished for this question as it is a bonus.")
    
    print("\nThat's the end.  Let's see how you did...")
    print("You answered {} questions, got {} wrong, and got {} right.".format(amtofquestions,wrong,right))
    if bonusright is True:
        print("You also got the bonus right, which is where the additional right answer came from.")
    grade = int(round((right/amtofquestions)*100, 0))
    if grade <= 69: 
        print("You would have gotten a grade of {}%.  That's a failing grade.  You lose.".format(grade))
    elif grade == 100:
        print("You got a perfect score.  Great work.")
    elif grade > 69:
        print("You would have gotten a grade of {}%.  That's a passing grade.  You win.".format(grade))

again = "null"
while again == "null":
    quiz()
    while again != "y" and again != "n":
        again = str.lower(input("Would you like to restart? y or n: "))
    if again == "y":
        again = "null"
    elif again == "n":
        print("Alright.  Thanks for playing.")

#CHANGELOG! (since V1)
#Questions are now stored as keys in a dictionary (qlist) with their answers as the values of the keys
#The order in which the questions are presented is now random
#There's a grade calculator at the end now to determine win/lose
#The program is an insomniac now.  No time.sleep()'s
#This program does everything V1 did, but in soooooooo many less lines
