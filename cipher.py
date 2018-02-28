# this program cannot be run independently
# this is a library used by cipherFrontend
import string
alpha = list(string.ascii_lowercase)
greenelist = list('!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~')

def showLauncher(): # display function selection menu
    print("============Launcher============")
    print("1 ------------- Encrypt from CLI")
    print("2 ------------- Decrypt from CLI")
    print("3 ------- Encrypt from text file")
    print("4 ------- Decrypt from text file")
    print("5 --------- Brute Force from CLI")
    print("6 --- Brute Force from text file")
    print("7 ------ Reverse Cipher from CLI")
    print("8  Reverse Cipher from text file")
    print("9 ------------------------- Exit")
    print("================================")

def getKey(): # ask user for key, loops until key is valid
    badKey = True
    while badKey is True:
        try:
            usrKey = int(input("Key: "))
            return usrKey
            badKey = False
        except ValueError:
            print("Bad key type")

def encrypt(usr, key): # takes string and key, returns encrypted list
    ls = list(usr)
    newls = []
    for letter in ls:
        # if not letter.isalpha():
        #     newls.append(letter)
        # else:
        if letter.isupper():
            newls.append(greenelist[(greenelist.index(letter.lower())+key)%95].upper())
        else:
            newls.append(greenelist[(greenelist.index(letter)+key)%95])
    return newls

def decrypt(encrypted, key): # takes string and key, returns decrypted list
    ls = list(encrypted)
    newls = []
    for letter in ls:
        # if not letter.isalpha():
        #     newls.append(letter)
        # else:
        if letter in greenelist:
            if letter.isupper():
                newls.append(greenelist[(greenelist.index(letter.lower())-key)%95].upper())
            else:
                newls.append(greenelist[(greenelist.index(letter)-key)%95])
        else: newls.append(letter)
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

def removePunctuation(ls): # takes in a list and returns the same list without punctuation
    for i in ls:
        if i in string.punctuation:
            ls.remove(i)
    return ls

def bruteforce(encrypted, usrRunthrus): # takes in an encrypted string and finds possible keys and decryptions
    runthrus = usrRunthrus
    knownkeys = []
    results = []
    while runthrus != 0:
        try:
            dictionary = open("dict.txt","r")
            dictionaryls = []
            for word in dictionary:
                dictionaryls.append(word.rstrip())
            done = False
            while done is False:
                print("POSSIBLE DECRYPTIONS AND KEYS: ")
                for key in range(0,26):
                    decryptedwords = "".join(removePunctuation(decrypt(encrypted, key))).split()
                    print("".join(decrypt(encrypted, key)))
                    print(f"Key: {key}")
                    knownkeys.append(key)
                    results.append("".join(decrypt(encrypted, key)))
                    done = True
                if len(knownkeys) == 0:
                    print("Could not decrypt, input is likely gibberish or composed solely of proper nouns")
                    done = True
        except FileNotFoundError:
            print("ERROR: The dictionary file could not be found and is necessary for this function to work")
            break
        if runthrus > 1:
            input(f"Entering runthru #{runthrus}")
            for result in results:
                input(f"BRUTEFORCING: {result}")
                bruteforce(result, 1)
            runthrus -= 1
        else: break

def bruteforceFromFile(filename):
    try:
        txtfile = open(f"{filename}.txt")
        contents = txtfile.read().rstrip("\n").lower()
        txtfile.close()
        print("WARNING!  Using brute force on a text file with an excessive amount of content,")
        print("specifically the entire Bee Movie script, will likely take a very long time.")
        warning = "bob"
        while warning != "y" and warning != "n":
            warning = input("Do you still wish to continue? y or n: ")
            if warning == "y":
                bruteforce(contents, 1)
    except FileNotFoundError:
        print("ERROR: File Not Found")

def reverseCipher(usr):
    return list(usr)[::-1]

def reverseCipherFromFile(filename):
    try:
        txtfile = open(f"{filename}.txt","r")
        contents = txtfile.read().rstrip("\n").lower()
        txtfile.close()
        print("".join(reverseCipher(contents)))
    except FileNotFoundError:
        print("ERROR: File Not Found")

if __name__ == "__main__": # this happens when someone tries to run cipher.py on its own
    print("This program cannot be executed independenly as it is a library on which")
    print("cipherFrontend relies.  Please run cipherFrontend.py")
