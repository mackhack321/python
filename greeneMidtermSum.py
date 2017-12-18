#If this program throws a syntax error on launch, you're not running in Python 3.6 or higher.
#This program will not work on an interpreter earlier than 3.6, due to the use of formatting with f"{}",
#a feature implemented in Python 3.6

ls = [0,1,2,3,4,5]
def forSum():
    forList = []
    for i in ls:
        forList.append(i)
    a = sum(forList)
    return(a)

def whileSum():
    whileList = []
    while len(whileList) != len(ls):
        for i in ls:
            whileList.append(i)
    a = sum(whileList)
    return(a)

print(f"Numbers to be Summed: {ls}")
print(f"This sum was found using for: {forSum()}")
print(f"This sum was found using while: {whileSum()}")
input()
