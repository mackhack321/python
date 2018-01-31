hourly = float(8.25)

med = float(.0145)
fed = float(.0196)
#fed = int(0)
social = float(.062)
union = float(8.11)

hours = float(input("How many hours to calculate for?"))

def paycheck():
    gross = round(float(hours*hourly), 2)
    print("Your gross earning is $"+str(gross)+".")
    
    net = round(float(gross-(gross*med)-(gross*fed)-(gross*social)-union), 2)
    print("You net earning is $"+str(net)+".")

paycheck()
