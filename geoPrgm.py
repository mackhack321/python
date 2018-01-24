try:
    import geoFunctions as mack
    badImport = False
except ImportError:
    print("You do not have the necessary modules for this program to work.")
    print("This program is not compatiable with your machine")
    badImport = True

def launcher():
    print("============Launcher============")
    print("1 ------------- Find Circle Area")
    print("2 --------------- Find Rect Area")
    print("3 ---- Find Circle Circumference")
    print("4 ------------------------ About")
    print("5 ------------------------- EXIT")
    print("================================")
    choice = input("Enter the number of your choice: ")
    if choice == "1":
        mack.areaOfCircle()
        launcher()
    elif choice == "2":
        mack.areaOfRec()
        launcher()
    elif choice == "3":
        mack.circumOfCircle()
        launcher()
    elif choice == "4":
        mack.about()
        launcher()
    elif choice == "5":
        pass
    else:
        launcher()
if badImport is True:
    pass
else:
    launcher()
