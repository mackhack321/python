import string
alpha = list(string.ascii_lowercase)

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
                newIndex = 26 - newIndex
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

usrString = input("Text to encode: ")
usrKey = int(input("Key: "))
print("".join(encrypt(usrString, usrKey)))
usrString = input("Text to decode: ")
usrKey = int(input("Key: "))
print("".join(decrypt(usrString, usrKey)))
