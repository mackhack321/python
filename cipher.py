import string
alpha = list(string.ascii_lowercase)

def showLauncher():
    print("============Launcher============")
    print("1 ------------- Encrypt from CLI")
    print("2 ------------- Decrypt from CLI")
    print("3 ------- Encrypt from text file")
    print("4 ------- Decrypt from text file")
    print("5 ------------------------- Exit")
    print("================================")

def getKey():
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

def encrypt(usr, key):
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

def decrypt(encrypted, key):
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

def encryptFromFile(filename, key):
    try:
        read = open(f"{filename}.txt", "r")
        contents = read.read().rstrip("\n").lower()
        read.close()
        write = open(f"{filename}.txt","w")
        encrypted = encrypt(contents, key)
        write.write("".join(encrypted))
        print("Done!")
    except FileNotFoundError:
        print("ERROR: Specified file could not be found")

def decryptFromFile(filename, key):
    try:
        read = open(f"{filename}.txt", "r")
        contents = read.read().rstrip("\n").lower()
        read.close()
        write = open(f"{filename}.decrypted.txt","w")
        decrypted = decrypt(contents, key)
        write.write("".join(decrypted))
        print("Done!")
    except FileNotFoundError:
        print("ERROR: Specified file could not be found")
