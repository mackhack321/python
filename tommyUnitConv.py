unit = input("Millimeter or Centimeter? m or c\n")
amt = float(input("Give the measurement.\n"))

if unit == "m":
    inch = float((1/25.4)*amt)
    print("{} millimeters is {} inches.".format(amt,inch))
if unit == "c":
    inch = float((1/2.54)*amt)
    print("{} centimeters is {} inches.".format(amt,inch))
