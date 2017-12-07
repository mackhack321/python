numbers = []
numberOne = input("Give one number")
numbers.append(numberOne)
numberTwo = input("Give another number")
numbers.append(numberTwo)

whichOp = input("Add, sub, mul, or div?")

if whichOp == "list":
    print(numbers)
if whichOp == "add":
    print(int(numberOne) + int(numberTwo))
if whichOp == "sub":
    print(int(numberOne) - int(numberTwo))
if whichOp == "mul":
    print(int(numberOne) * int(numberTwo))
if whichOp == "div":
    print(int(numberOne) / int(numberTwo))

