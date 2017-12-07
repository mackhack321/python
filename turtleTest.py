import turtle as t
win = t.Screen()

def color():
    color = str.lower(input("Color: "))
    try:
        t.fillcolor(color)
        t.begin_fill()
    except t.TurtleGraphicsError:
        print("ERROR: Invalid Color")

def reset():
    t.reset()

def clear():
    t.clear()

def move():
    try:
        dir = input("Direction? l, r, or n: ")
        if dir != "n":
            dirAmt = int(input("How much?: "))
        movAmt = int(input("How much forward?: "))
        t.up()
        if dir == "l":
            t.left(dirAmt)
            t.forward(movAmt)
        elif dir == "r":
            t.right(dirAmt)
            t.forward(movAmt)
        elif dir == "n":
            t.forward(movAmt)
        t.down()
    except ValueError:
        print("ERROR: Invalid Value")
    

def rect():
    for i in range(2):
        t.forward(200)
        t.left(90)
        t.forward(100)
        t.left(90)
    stop = input("Stop the fill? y or n: ")
    if stop == "y":
        t.end_fill()

def tri():
    for i in range(3):
        t.forward(100)
        t.left(120)
    stop = input("Stop the fill? y or n: ")
    if stop == "y":
        t.end_fill()

def square():
    for i in range(4):
        t.forward(100)
        t.left(90)
    stop = input("Stop the fill? y or n: ")
    if stop == "y":
        t.end_fill()

def circle():
    rad = int(input("Radius: "))
    t.circle(rad)
    stop = input("Stop the fill? y or n: ")
    if stop == "y":
        t.end_fill()

def para():
    t.forward(200)
    t.left(45)
    t.forward(100)
    t.left(135)
    t.forward(200)
    t.left(45)
    t.forward(100)
    stop = input("Stop the fill? y or n: ")
    if stop == "y":
        t.end_fill()

def g59():
    #import turtle as t
    t.hideturtle()
    t.up()
    t.left(180)
    t.forward(100)
    t.right(180)
    t.down()
    t.pensize(5)
    for i in range(5):
        t.forward(190)
        t.right(144)
    
    t.up()
    t.backward(6.8)
    t.right(90)
    t.forward(32)
    t.down()
    t.circle(100.8)

    t.up()
    t.right(90)
    t.forward(350)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.down()
    t.write("SEE THROUGH THE FEAR", move=False, align="left", font=('Old English Text MT',40,'normal'))
    t.up()
    t.right(90)
    t.forward(275)
    t.left(90)
    t.forward(50)
    t.write("GREYFIVENINE", move=False, align="left", font=('Old English Text MT',40,'normal'))

def star():
    for i in range(5):
        t.forward(200)
        t.right(144)


