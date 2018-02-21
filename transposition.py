# "the quick brown fox" with key of 5: tub hirfecoo kwxq n|
# "pure imagination" with key of 5: pinnuma|rat|egi| io|
# "Mack has found out something neat: Transposition encryption!" with key of 4:
# M  nuoh trpt riahfdtmin:aoieyocao  ene nsonpnksuostgaTsinct!
# "mack is the best" with key of 6: msba ectskht e|i |

# run the program with --showArray to see the encryption grid
from math import ceil # this is needed to round up
from sys import argv # this lets us see the command line args
import pyperclip as pclip

def showArrayIfArg(ls): # this takes in a raw list and, if the arg is present, displays each item in the list
     try:
         if "--showArray" in argv:
             for i in bigls:
                 print(i)
     except: pass

def encrypt(usr, key):
    usrls = list(usr)
    rows = ceil(len(usr)/key)
    numOfChars = len(usrls)
    counter = 0

    bigls = []
    rowls = []
    encryptedls = []

    while counter != rows:
        newls = usrls[0+(key*counter):key+(key*counter)]
        while len(newls) != key:
            newls.append("|")
        bigls.append(newls)
        counter += 1

    for num in range(key):
        encryptedls.append("".join(i[num] for i in bigls))

    showArrayIfArg(bigls) # debug
    return encryptedls # this function returns a raw list!!! it is up to the frontend to make it pretty

def decrypt(encrypted, key):
    encryptedls = list(encrypted)
    rows = ceil(len(usr)/key)
    decryptedls = []
    for i in range(0,rows):
        for ls in encryptedls[i::rows]: # need to find the right splice
            decryptedls.append(ls)
            showArrayIfArg(ls) # debug
        decryptedls = [i for i in decryptedls if i != "|"]
    return decryptedls # this function returns a raw list!!! it is up to the frontend to make it pretty

def getKey():
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
if choice == "e":
    usr = input("Message to encrypt: ")
    key = getKey()
    print("".join(encrypt(usr,key)))
    copy = input("Copy to clipboard? y/n: ")
    if copy == "y":
        try:
            pclip.copy("".join(encrypt(usr,key)))
            print("Copied!")
        except NotImplemented:
            print("ERROR: Copy is not implemented on your machine")
if choice == "d":
    usr = input("Message to decrypt: ")
    key = getKey()
    print("".join(decrypt(usr, key)))
    copy = input("Copy to clipboard? y/n: ")
    if copy == "y":
        try:
            pclip.copy("".join(decrypt(usr,key)))
            print("Copied!")
        except pclip.PyperclipException:
            print("ERROR: Copy is not implemented on your machine")
