# while counter < numOfChars:
#     for i in range(counter,key):
#         print(counter)
#         rowls.append(usrls[i])
#         counter += 1
#     bigls.append(rowls)
#     print(rowls)

# print(usrls[0:key]) # ['t', 'h', 'e', ' ', 'q']
# print(usrls[0+key:key+key]) # ['u', 'i', 'c', 'k', ' ']
# print(usrls[0+key+key:key+key+key]) # ['b', 'r', 'o', 'w', 'n']
from math import ceil # this is needed to round up
def encrypt(usr, key):
    usrls = list(usr)
    bigls = []
    rows = ceil(len(usr)/key)
    numOfChars = len(usrls)
    rowls = []
    encryptedls = []
    counter = 0

    while counter != rows:
        newls = usrls[0+(key*counter):key+(key*counter)]
        while len(newls) != key:
            newls.append("|")
        bigls.append(newls)
        counter += 1

    for num in range(key):
        encryptedls.append("".join(i[num] for i in bigls))

    return encryptedls

def decrypt(encrypted,key):
    decryptedls = []
    counter = 0
    while counter != len(bigls):
        for ls in bigls:
            decryptedls.append(ls[0])
            counter += 1
    print(decryptedls)

def toList(msg,key):
    bigls = []
    newls = []
    rows = ceil(len(msg)/key)
    while counter != rows:
        newls = usrls[0+(key*counter):key+(key*counter)]
        bigls.append(newls)
    return(bigls)

usr = input("Message to encrypt: ")
key = int(input("Key: "))
print("".join(encrypt(usr,key)))
