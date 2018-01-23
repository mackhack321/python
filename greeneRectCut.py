# the end of a python range is 1 less than the given value. range(3) = 0,1,2
# def cutit(h,w):
#     dir = ((1,0),(-1,0),(0,-1),(0,1))
#     if h & 1:
#         h,w = w,h
#     if h & 1:
#         return 0
#     if w == 1:
#         return 1
#     count = 0
#
#     next = [w + 1,-w-1,-1,1]
#     bl = (h + 1) * (w + 1) - 1
import random
height = 3
width = 4
def checkPath():
    pass
    #here, I want to check if the path actually cuts the shape in equal parts
    #problem is, I have no idea how to do that
    #possibly by spliting the list of directions in half
    #and comparing the items/lengths of the two?
    #who knows
    #not me
def makePath():
    ls = ["r","r","r","r","r","r","r"]
    while ls.count("d") != 3:
        rand = random.randint(0,6)
        if ls[rand] == "d":
            continue
        else:
            ls[rand] = "d"
    return ls
solutions = []
while len(solutions) != 10:
    solutions.append(makePath())
for i in solutions:
    print(i)
