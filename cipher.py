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

def getUsrArgs():
    badKey = True
    while badKey is True:
        try:
            usrString = input("Text to encode: ")
            usrKey = int(input("Key: "))
            if usrKey == 0 or usrKey > 25:
                print("Bad key")
                continue
            print("".join(encrypt(usrString, usrKey)))
            usrString = input("Text to decode: ")
            usrKey = int(input("Key: "))
            if usrKey == 0 or usrKey > 25:
                print("Bad key")
                continue
            print("".join(decrypt(usrString, usrKey)))
            badKey = False
        except ValueError:
            print("Bad key type")

def encryptFromFile(filename, key):
    read = open(f"{filename}.txt", "r")
    contents = read.read().rstrip("\n")
    read.close()
    write = open(f"{filename}.txt","w")
    encrypted = encrypt(contents, key)
    write.write("ENCRYPTED:\n")
    write.write("".join(encrypted))
    write.write("\nDECRYPTED:\n")
    write.write("".join(decrypt(encrypted, key)))
