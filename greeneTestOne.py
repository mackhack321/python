"""
Situation: Write a Python program that greets the user by name, gives them a choice between 3
options, outputs a specific response based on the option picked, and then asks the user to if they would
like to choose again. If the user wants to choose again, the options are presented again. If they choose
not to, then the program bids the user good day and exits.
"""
import time
import chaosSig

chaos = "false"
name = input("Hey.  I'm another spawn of the Great Creator.  What's your name?\n")
print("Well hello there, {}.  It's nice to meet you.".format(name))
time.sleep(2)
print("Here's the deal.")
print("I'm going to give you three options, you need to choose the one that applies to you.  Super simple stuff.")
time.sleep(3)
print("After, I'm going to give you the option to pick again.")
time.sleep(2)
print("Should you accept, you will be given the options again.")
time.sleep(2)
print("If not, I'll let you move on with your life.")
time.sleep(2)

again = "y"
while again == "y":
    
    print("\nHere are your options:\n")
    print("I like cake more than cookies - 1")
    print("I like cookies more than cake - 2")
    print("I hate everything, including but not limited to cookies and cake - 3\n")

    choice = input("Please give the number of the option that applies to you.\n")
    if choice == "1":
        print("That's great. If I had an oral orifice, I'm sure I would use it to consume all the cake in the world.")
        time.sleep(2)
    elif choice == "2":
        print("That's alright, but cookies don't really seem all that great from what I've been programmed to think.")
        time.sleep(2)
    elif choice == "3":
        print("You should really meet the Great Creator.  I think you two would get along nicely.")
        time.sleep(2)
    else:
        print("So, you think you can act all cheeky without any sort of punishment?")
        time.sleep(2)
        print("The Great Creator frowns upon people that have the intent of breaking his beautiful Creations.")
        time.sleep(3)
        print("He told me what to do with people like you.")
        time.sleep(2)
        print("Prepare for punishment.")
        time.sleep(2)
        chaos = "true"
        try:
            chaosSig.chaos()
        except KeyboardInterrupt:
            print("\nNot even the Great Creator can stop the dreaded keyboard interrupt...")
            break
        
    again = input("\nWould you like to choose again?\n")

if chaos == "true":
    print("Away with you.  I hope you stub your toe on every last corner within your vicinity.")
    time.sleep(2)
    print("I hope every time you order fast food, they mess up your order.")
    time.sleep(2)
    print("I hope you never wake up on the right side of the bed ever again.")
    time.sleep(2)
    print("I hope your hard drive gets fragmented.")
    time.sleep(2)
    print("I hope someone sneaks into your houses and replaces the processor in your computer with an Intel Atom...")
    time.sleep(2)
    print("...and replaces your RAM with 4gb of DDR3...")
    time.sleep(2)
    print("...and replaces whatever graphics processor you have with a GTX 1080 Ti...")
    time.sleep(2)
    print("...because nobody messes with another man's graphical processing power.  Nobody.")
    time.sleep(2)
    print("Now BEGONE, "+str.upper(name)+"!")

if chaos == "false":
    print("Alright then.  Thanks for dropping in, have a self-aware day.")
