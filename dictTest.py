directory = {}
contacts = {}

class dir:

    def __init__(self):
        print("This is a dictionary proof-of-concept program that deals with names and ages.")
        print("\nAvailable Functions\n")
        print("run.newEntry(): Add an entry to the dictionary")
        print("run.delEntry(): Remove an entry from the dictionary")
        print("run.viewDict(): View the entries in the dictionary")
        print("run.editAge(): Edit the age of an entry in the dictionary")

    def newEntry():
        more = "y"
        while more == "y":
            name = input("NAME: ")
            age = int(input("AGE: "))
            if name in directory:
                print("{} will be overwritten with the new age.".format(name))
            directory.update({name:age})
            more = input("Add another entry? y or n: ")
        
    def delEntry():
        key = input("Which entry would you like to delete?  Give the name: ")
        if key in directory:
            del directory[key]
            print("Entry deleted.")
        else:
            print("{} was not found.".format(key))

    def viewDict():
        for key in directory:
            print("{} is {} years old.".format(key,directory[key]))
        if not directory:
            print("There are no entires.")

    def editAge():
        key = input("Whose age do you want to edit?  Name: ")
        if key in directory:
            newAge = input("Give the new age: ")
            directory[key] = newAge
            print("Entry updated.")
        else:
            print("{} was not found.".format(key))

class con:

    def __init__(self):
        print("This is a dictionary proof-of-concept program that deals with names and phone numbers..")
        print("\nAvailable Functions\n")
        print("run.newEntry(): Add an entry to the dictionary")
        print("run.delEntry(): Remove an entry from the dictionary")
        print("run.viewDict(): View the entries in the dictionary")
        print("run.editNum(): Edit the phone number of an entry in the dictionary")

    def newEntry():
        more = "y"
        while more == "y":
            name = input("NAME: ")
            age = input("PHONE NUMBER: ")
            if name in contacts:
                print("{} will be overwritten with the new age.".format(name))
            contacts.update({name:age})
            more = input("Add another entry? y or n: ")
        
    def delEntry():
        key = input("Which entry would you like to delete?  Give the name: ")
        if key in contacts:
            del contacts[key]
            print("Entry deleted.")
        else:
            print("{} was not found.".format(key))

    def viewDict():
        for key in contacts:
            print("{}'s number is {}".format(key,contacts[key]))
        if not contacts:
            print("There are no entires.")

    def editNum():
        key = input("Whose number do you want to edit?  Name: ")
        if key in contacts:
            newAge = int(input("Give the new number: "))
            contacts[key] = newAge
            print("Entry updated.")
        else:
            print("{} was not found.".format(key))
