#Mack Stanley, Joey Pike, Grayson Jordan, Aidan Sanders
import time

def quiz():
    wrong = 0
    right = 0
    bonus = 0

    print("Hey hey hey, player!  Gimme a name to call you by.")
    name = input("Enter your name: ")
    print("What's up, {}?  This is a trivia game all about Python!".format(name))
    time.sleep(2)
    print("All the questions are true/false.  Put t for true and f for false.")
    time.sleep(2)
    print("Let's get right to it then!")
    time.sleep(2)
    if name == "debug":
        print("...but first, the debug menu.")
        print("---DEBUG MENU---")
        print("ʕ•ᴥ•ʔ ʕ•ᴥ•ʔ ʕ•ᴥ•ʔ ʕ•ᴥ•ʔ")
        print("1 - Set Right to number\n2 - Set Wrong to number")
        choice = input("Pick an option.\n")
        if choice == "1":
            num = int(input("Set Right to what amount?\n"))
            right = right + num
            print("Var 'right' has been set to {}.".format(num))
        elif choice == "2":
            num = int(input("Set Wrong to what amount?\n"))
            wrong = wrong + num
            print("Var 'wrong' has been set to {}.".format(num))
        else:
            print("Invalid option given.")
        print("NOW, let's get right to it then!")

    print("---STATEMENT ONE---")
    print("A global variable can become a local variable.")
    ans = input("t or f?\n")
    if ans == "t":
        print("Ding ding ding!  You got it!")
        right = right + 1
    elif ans == "f":
        print("Oops...that's not it...the statement is true!")
        wrong = wrong + 1
    else:
        print("{} wasn't an option.  That counts as wrong.  Follow the rules, man.".format(ans))
        wrong = wrong + 1
    time.sleep(2)

    print("---STATEMENT TWO---")
    print("A local variable can become a global variable.")
    ans = input("t or f?\n")
    if ans == "f":
        print("Nice one!")
        right = right + 1
    elif ans == "t":
        print("Nope...the statement is false!")
        wrong = wrong + 1
    else:
        print("{} wasn't an option.  That counts as wrong.  Follow the rules, man.".format(ans))
        wrong = wrong + 1
    time.sleep(2)

    print("---STATEMENT THREE---")
    print("Python is an interpreted language.")
    ans = input("t or f?\n")
    if ans == "t":
        print("Yep.  Python runs one line at a time.")
        right = right + 1
    elif ans == "f":
        print("Wrong...the statement is true!")
        wrong = wrong + 1
    else:
        print("{} wasn't an option.  That counts as wrong.  Follow the rules, man.".format(ans))
        wrong = wrong + 1
    time.sleep(2)

    print("---STATEMENT FOUR---")
    print("print(apple) would print the word apple to the screen.")
    ans = input("t or f?\n")
    if ans == "f":
        print("Right!  You need to add quotation marks around apple.")
        right = right + 1
    elif ans == "t":
        print("Nope...because there aren't any quotation marks, Python thinks that's a variable.")
        wrong = wrong + 1
    else:
        print("{} wasn't an option.  That counts as wrong.  Follow the rules, man.".format(ans))
        wrong = wrong + 1
    time.sleep(2)

    print("---STATEMENT FIVE---")
    print("print 'Hello, world!' would print Hello, world! to the screen in Python 2.")
    ans = input("t or f?\n")
    if ans == "t":
        print("That's right!  In Python 2, you don't need the ()'s!")
        right = right + 1
    elif ans == "f":
        print("Wrong!  That would work just fine.")
        wrong = wrong + 1
    else:
        print("{} wasn't an option.  That counts as wrong.  Follow the rules, man.".format(ans))
        wrong = wrong + 1
    time.sleep(2)

    print("---STATEMENT SIX---")
    print("You can get paid for being a Python programmer.")
    ans = input("t or f?\n")
    if ans == "t":
        print("Yep!  Plenty of people would pay you to code in Python for them.")
        right = right + 1
    elif ans == "f":
        print("That's not right.  Programmers are in pretty high demand right now.")
        wrong = wrong + 1
    else:
        print("{} wasn't an option.  That counts as wrong.  Follow the rules, man.".format(ans))
        wrong = wrong + 1
    time.sleep(2)

    print("---STATEMENT SEVEN---")
    print("\\n makes a new line and \\t is equivalent to hitting the tab key.")
    ans = input("t or f?\n")
    if ans == "t":
        print("That's right!  Those are called escape characters, and there are lots more than two.")
        right = right + 1
    elif ans == "f":
        print("Wrong!  Those are escape characters, and their specified functions are true.")
        wrong = wrong + 1
    else:
        print("{} wasn't an option.  That counts as wrong.  Follow the rules, man.".format(ans))
        wrong = wrong + 1
    time.sleep(2)

    print("---STATEMENT EIGHT---")
    print("'and', 'or', and 'in' are all examples of operators.")
    ans = input("t or f?\n")
    if ans == "f":
        print("Good job!  Those are booleans, not operators.")
        right = right + 1
    elif ans == "t":
        print(":( Those are booleans, not operators.")
        wrong = wrong + 1
    else:
        print("{} wasn't an option.  That counts as wrong.  Follow the rules, man.".format(ans))
        wrong = wrong + 1
    time.sleep(2)

    print("---STATEMENT NINE---")
    print("apple == 'HI!' would assign 'HI!' to variable 'apple'.")
    ans = input("t or f?\n")
    if ans == "f":
        print("That's right!  == compares and = assigns.")
        right = right + 1
    elif ans == "t":
        print("Nein!  == compares and = assigns.")
        wrong = wrong + 1
    else:
        print("{} wasn't an option.  That counts as wrong.  Follow the rules, man.".format(ans))
        wrong = wrong + 1
    time.sleep(2)

    print("---STATEMENT TEN---")
    print("A NameError happens when you reference a variable that hasn't been defined.")
    ans = input("t or f?\n")
    if ans == "t":
        print("Yep!")
        right = right + 1
    elif ans == "f":
        print("Nope, that statement is true.")
        wrong = wrong + 1
    else:
        print("{} wasn't an option.  That counts as wrong.  Follow the rules, man.".format(ans))
        wrong = wrong + 1
    time.sleep(2)

    print("---!!BONUS QUESTION!!---")
    print("What does IDE stand for?")
    ans = str.lower(input("This is the only question that needs an actual answer, not true/false.\n"))
    if ans == "integrated development environment":
    #IF my beautiful program has an achilles heel, it's here.
        print("Awesome!  That's the name for whatever program you actually type code in.  You get two points for that one!")
        bonus = 1
    else:
        print("Sorry, that's not it.  IDE stands for Integrated Development Environment.  That answer won't hurt you since it's a bonus.")
    time.sleep(2)

    print("That's the end of the game!  Let's see how you did...")
    time.sleep(2)
    print("You got {} question(s) correct...".format(right))
    time.sleep(2)
    print("...and {} question(s) wrong.".format(wrong))
    time.sleep(2)
    if bonus == 1:
        print("You also got the bonus right, so that counts for 2 right answers.")
        right = right + 2
        print("Final Score: {} right and {} wrong.".format(right,wrong))
    if right > wrong:
        print("You got the majority of questions right, which means you win!  Nice job, {}!".format(name))
    if right < wrong:
        print("Sorry...you got the majority of those wrong.  You lose this time, {}.".format(name))
    if right == wrong:
        print("You got the same amount of questions wrong as you did right.  How average.")
    time.sleep(2)

again = "y"
while again == "y":
    quiz()
    again = input("Play again?  The questions won't be any different so I don't know why you would, but the choice is yours. y or n\n")
    if again == "y":
        pass
    elif again == "n":
        print("Alright.  Thanks for playing!")
    else:
        print("{} wasn't an option.  Go away.".format(again))
        time.sleep(2)
