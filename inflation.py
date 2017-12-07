print("This is a simple, chaos-free inflation calculator.")
year = input("Give a year. 2000-2016")
amount = input("Give an amount of money in decimal form.  No dollar sign.")

def calc(percentage):
    inflated = round(float(amount)-(float(amount)*float(percentage)), 2)
    print("$"+str(amount)+" would be worth "+"$"+str(inflated)+" in "+year+".")

if year == "2000":
    calc(.0338)
elif year == "2001":
    calc(.0155)
elif year == "2002":
    calc(.0238)
elif year == "2003":
    calc(.0227)
elif year == "2004":
    calc(.0268)
elif year == "2005":
    calc(.0339)
elif year == "2006":
    calc(.0324)
elif year == "2007":
    calc(.0285)
elif year == "2008":
    calc(.0385)
elif year == "2009":
    calc(.0034)
elif year == "2010":
    calc(.0164)
elif year == "2011":
    calc(.0316)
elif year == "2012":
    calc(.0207)
elif year == "2013":
    calc(.0147)
elif year == "2014":
    calc(.0162)
elif year == "2015":
    calc(.0012)
elif year == "2016":
    calc(.0126)
elif year == "2017":
    calc(.0215)

else:
    print(year+" is not a valid year.")
