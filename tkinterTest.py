from tkinter import *
import tkinter.messagebox as tm

root = Tk()

def onLClick(event):
    print("Click!")

def foobar():
    print("foobar")

def apple():
    print("apple")

def msgbox():
    tm.showinfo('Message Box','This information is useless')

def ask():
    ans = tm.askquestion('Question','Do you like apples?')
    if ans == "yes":
        print("Me too")
    if ans == "no":
        print(":( but they're good")

frame = Frame(width="300",height="200")
frame.pack()

labelOne = Label(frame, text="I am a label")
labelOne.pack()

buttonOne = Button(frame, text="I am a button", fg="purple", bg="cyan")
buttonOne.bind("<Button-1>", onLClick)
buttonOne.pack(side=LEFT)

quitButton = Button(frame, text="QUIT", fg="red", bg="yellow", command=root.destroy)
quitButton.pack(side=LEFT)

menuOne = Menu(root)
root.config(menu=menuOne)

subMenu = Menu(menuOne)
menuOne.add_cascade(label="Print", menu=subMenu)
subMenu.add_command(label="Print foobar",command=foobar)
subMenu.add_command(label="Print apple",command=apple)

mesMenu = Menu(menuOne)
menuOne.add_cascade(label="Msg Box", menu=mesMenu)
mesMenu.add_command(label="Show the box",command=msgbox)
mesMenu.add_command(label="Ask the question",command=ask)

root.mainloop()
