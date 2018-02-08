# this program cannot be run independently
# this is a library used by cipherFrontend
import string
alpha = list(string.ascii_lowercase)

def showLauncher(): # display function selection menu
    print("============Launcher============")
    print("1 ------------- Encrypt from CLI")
    print("2 ------------- Decrypt from CLI")
    print("3 ------- Encrypt from text file")
    print("4 ------- Decrypt from text file")
    print("5 ------------------------- Exit")
    print("================================")

def getKey(): # ask user for key, loops until key is valid
    badKey = True
    while badKey is True:
        try:
            usrKey = int(input("Key: "))
            if usrKey == 0 or usrKey > 25:
                print("Bad key")
                continue
            return usrKey
            badKey = False
        except ValueError:
            print("Bad key type")

def encrypt(usr, key): # takes string and key, returns encrypted list
    ls = list(usr)
    newls = []
    for letter in ls:
        if not letter.isalpha():
            newls.append(letter)
        else:
            try:
                index = alpha.index(letter)
                newIndex = index + key
                newls.append(alpha[newIndex])
            except IndexError:
                newIndex = newIndex - 26
                newls.append(alpha[newIndex])
    return newls

def decrypt(encrypted, key): # takes string and key, returns decrypted list
    ls = list(encrypted)
    newls = []
    for letter in ls:
        if not letter.isalpha():
            newls.append(letter)
        else:
            index = alpha.index(letter)
            newIndex = index - key
            newls.append(alpha[newIndex])
    return newls

def encryptFromFile(filename, key): # takes filename and key, encrypts contents
    try:
        read = open(f"{filename}.txt", "r")
        contents = read.read().rstrip("\n").lower()
        read.close()
        ask = input("Would you like to\nA) overwrite the contents of this file\nor\nB) write to {filename}.encrypted.txt\na or b: ").lower()
        if ask == "a":
            write = open(f"{filename}.txt","w")
        elif ask == "b":
            write = open(f"{filename}.encrypted.txt","w")
        else:
            write = open("icantfollowdirectionsorimreallybadattyping.txt","w")
        encrypted = encrypt(contents, key)
        write.write("".join(encrypted))
        print("Done!")
    except FileNotFoundError:
        print("ERROR: Specified file could not be found")

def decryptFromFile(filename, key): # takes filename and key, decrypts contents
    try:
        read = open(f"{filename}.txt", "r")
        contents = read.read().rstrip("\n").lower()
        read.close()
        ask = input(f"Would you like to\nA) overwrite the contents of this file\nor\nB) write to {filename}.decrypted.txt\na or b: ").lower()
        if ask == "a":
            write = open(f"{filename}.txt","w")
        elif ask == "b":
            write = open(f"{filename}.decrypted.txt","w")
        else:
            write = open("icantfollowdirectionsorimreallybadattyping.txt","w")
        decrypted = decrypt(contents, key)
        write.write("".join(decrypted))
        print("Done!")
    except FileNotFoundError:
        print("ERROR: Specified file could not be found")

def bruteforce(encrypted):
    try:
        dictionary = open("dict.txt","r")
        dictionaryls = []
        for word in dictionary:
            dictionaryls.append(word.rstrip())
        done = False
        while done is False:
            for key in range(0,26):
                decrypted = decrypt(encrypted, key)
                decryptedstr = "".join(decrypted)
                decryptedwords = decryptedstr.split()
                for word in decryptedwords:
                    #print(word)
                    if word in dictionaryls:
                        print("".join(decrypted))
                        print(f"Key: {key}")
                        done = True
    except FileNotFoundError:
        print("The dictionary file could not be found and is necessary for this function to work")
