def charToNum(number):
    for i in number:
        if i.isdigit():
            return i
        elif i == "-":
            return i
        elif i in "ABC":
            return "2"
        elif i in "DEF":
            return "3"
        elif i in "GHI":
            return "4"
        elif i in "JKL":
            return "5"
        elif i in "MNO":
            return "6"
        elif i in "PQRS":
            return "7"
        elif i in "TUV":
            return "8"
        elif i in "WXYZ":
            return "9"

userNum = input("Give a word-number to decode: ").upper()
newNum = []
for i in userNum:
    newNum.append(charToNum(i))
print("".join(i for i in newNum))
