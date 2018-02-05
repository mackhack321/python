def getLine(line):
    txt = open("text.txt","r")
    lines = txt.readlines()
    print(lines[line - 1].rstrip("\n"))
    txt.close()

def addLine(line):
    txt = open("text.txt","a")
    txt.write(line)
    txt.close()
    return "Done!"

print("1) Get Line")
print("2) Add Line")
choice = input("Select a function: ")
if choice == "1":
    index = int(input("Give the line number you want: "))
    getLine(index)
elif choice == "2":
    usrline = input("String to add: ")
    print(addLine(usrline))
