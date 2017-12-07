def add():
    a = int(num1) + int(num2)
    print(a)
def sub():
    s = int(num1) + int(num2)
    print(s)
def mul():
    m = int(num1) + int(num2)
    print(m)
def div():
    d = int(num1) + int(num2)
    print(d)

print("This is a very crude caulculator program.\n")
num1 = input("Please give a number.\n")
num2 = input("Please give another number.\n")

op = input("Please give an operation to perform on the numbers. (add, sub, mul, or div)\n")

if op == "add":
    add()
if op == "sub":
    sub()
if op == "mul":
    mul()
if op == "div":
    div()
