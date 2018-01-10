#the end of a python range is 1 less than the given value. range(3) = 0,1,2
from random import randint
possibleRights = width = 4
possibleDowns = height = 3
ls = ["r","r","r","r","r","r","r","r","r","r"]
answers = []
while len(answers) != 9:
    for i in range(possibleDowns):
        rand = randint(0,len(ls) - 1)
        if ls[rand] != "d":
            ls[rand] = "d"
        else:
            i = i - 1
            continue
        if ls not in answers:
            answers.append(ls)
        else:
            continue
        print(ls)
print(answers)
