# run the program with argument --showArray to see the encryption grid
from math import ceil # this is needed to round up
from sys import argv # this lets us see the command line args
try:
    import pyperclip as pclip
    hasPyperclip = True # this lets the program know whether or not pyperclip is present
except ImportError: # print a friendly advisory message but dont break the program
    print("The pyperclip library is not installed on this machine.  Some functionality will not be available.")
    hasPyperclip = False

def askToCopy(hasPyperclip, result): # this only does anything if pyperclip is present
    if hasPyperclip is True:
        copy = input("Copy result to clipboard? y/n: ")
        if copy == "y":
            try:
                pclip.copy(result)
                print("Copied!")
            except NotImplemented:
                print("ERROR: Copy is not implemented on your machine")

def showArrayIfArg(ls): # this takes in a raw list and, if the arg is present, displays each item in the list
     try:
         if "--showArray" in argv:
             for i in ls:
                 print(i)
     except: pass

def encrypt(usr, key):
    usrls = list(usr) # turn input into a list
    rows = ceil(len(usr)/key) # find amount of rows that will be needed
    numOfChars = len(usrls) # get the length of the input
    counter = 0 # init counter
    bigls = [] # will contain lists that contain the string but cut up into 'rows' lists
    encryptedls = [] # will contain result

    while counter != rows: # each iteration of this loop creates a list that contains one row of the string
        newls = usrls[0+(key*counter):key+(key*counter)] # takes the input list and cuts it into a row with 'key' number of chars
        while len(newls) != key: # until there are no empty spots
            newls.append("|") # add a pipe to denote the empty spot
        bigls.append(newls) # add the freshly cut list to the big list
        counter += 1 # move on to the next row

    for num in range(key):
        encryptedls.append("".join(i[num] for i in bigls)) # add each list from the big list to the result list

    showArrayIfArg(bigls) # debug, shows the transposition grid
    return encryptedls # this function returns a raw list!!! it is up to the frontend to make it pretty

def decrypt(encrypted, key):
    encryptedls = list(encrypted) # turn input into a list
    rows = ceil(len(usr)/key) # find amount of rows that will be needed
    decryptedls = [] # will contain result
    for i in range(0,rows): # for all of the rows
        for char in encryptedls[i::rows]: # with every 'row'th char as ls
            decryptedls.append(char) # add the char to the result list
            showArrayIfArg(char) # debug, will show each char
        decryptedls = [i for i in decryptedls if i != "|"] # removes pipes from result list
    return decryptedls # this function returns a raw list!!! it is up to the frontend to make it pretty

def getKey(): # this gets and returns a key
    goodkey = False
    while goodkey is not True:
        key = int(input("Key: "))
        if key > len(usr):
            print("WARNING: Using a key that is larger than the lenght of your message will not encrypt anything.")
            confirm = input("Do you wish to continue? y or n: ")
            if confirm == "y":
                goodkey = True
                return key
            else:
                continue
        goodkey = True
        return key

choice = input("Encrypt or decrypt? e/d: ")
if choice == "e": mode = encrypt
elif choice == "d": mode = decrypt
usr = input("Message: ")
key = getKey()
result = "".join(mode(usr, key))
print(result)
askToCopy(hasPyperclip, result)
