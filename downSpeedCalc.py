def calc():
    if unit == "gb":
        toMB = size*1024
        final = (toMB / speed) / 60
        if final > 60:
            final = final / 60
            print("It will take {} minutes to download a {}{} file at a speed of {}mb/s.".format(round(final, 2),size,unit,speed))
        else:
            print("It will take {} minutes to download a {}{} file at a speed of {}mb/s.".format(round(final, 2),size,unit,speed))

    if unit == "mb":
        final = (size / speed) / 60
        if final > 60:
            final = final / 60
            print("It will take {} minutes to download a {}{} file at a speed of {}mb/s.".format(round(final, 2),size,unit,speed))
        else:
            print("It will take {} minutes to download a {}{} file at a speed of {}mb/s.".format(round(final, 2),size,unit,speed))

    else:
        print("{} is not a valid unit.".format(unit))

try:
    size = float(input("Give the numeric size of the file.\n"))
    unit = input("Give the unit. gb or mb\n")
    speed = float(input("Give the numeric downlaod speed in mb/s\n"))
    calc()
except ValueError:
    print("Invalid value.  Input numbers only.")
