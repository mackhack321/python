# "the quick brown fox" with key of 5: tub hirfecoo kwxq n|
# "pure imagination" with key of 5: pinnuma|rat|egi| io|
from math import ceil # this is needed to round up
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

    for i in bigls:
        print(i)
    return encryptedls

def decrypt(encrypted, key):
    encryptedls = list(encrypted)
    rows = rows = ceil(len(usr)/key)
    decryptedls = []
    for i in range(0,rows):
        for ls in encryptedls[i::4]:
            decryptedls.append(ls)
        decryptedls = [i for i in decryptedls if i != "|"]
    return decryptedls

choice = input("Encrypt or decrypt? e/d: ")
if choice == "e":
    usr = input("Message to encrypt: ")
    key = int(input("Key: "))
    print("".join(encrypt(usr,key)))
if choice == "d":
    usr = input("Message to decrypt: ")
    key = int(input("Key: "))
    print("".join(decrypt(usr, key)))
