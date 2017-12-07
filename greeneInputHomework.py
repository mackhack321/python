import chaosSig
import time
import sys
#assign the stuff
noun = input("Give a noun\n")
adj = input("Give an adjective\n")
verb = input("Give a verb in the progressive (-ing) tense\n")
adv = input("Give an adverb\n")
noun2 = input("Give another noun\n")
exc = input("Give an exclamatory for your noun to shout\n")
ch = input("Chaos? y or y")
if ch != "y":
    try:
        chaosSig.chaos()
    except KeyboardInterrupt:
        print("\nNoooo...my only weakness...a keyboard interrupt....")
        print("X.X")
        sys.exit()
#all together now
print("Once upon a time, there was a very {} {} that was {} when suddenly a(n) {} appeared!".format(adj,noun,verb,noun2))
print("The {} was very frightened by the {}.  It shouted '{}' and ran away.".format(noun,noun2,exc))
time.sleep(7)
try:
    chaosSig.chaos()
except KeyboardInterrupt:
    print("\nNoooo...my only weakness...a keyboard interrupt....")
    print("X.X")
