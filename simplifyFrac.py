from fractions import gcd

def simplify(num,denom):
    div = gcd(num,denom)
    newnum = num/div
    newdenom = denom/div
    if newnum == num and newdenom == denom:
        return "The fraction is already in simplest form"
    else:
        return f"Simplified: {newnum}/{newdenom}"

good = False
while good is False:
    try:
        num = int(input("Give the fraction's numerator: "))
        denom = int(input("Give the fraction's denominator: "))
        good = True
        print(simplify(num,denom))
    except ValueError:
        print("Bad input")
