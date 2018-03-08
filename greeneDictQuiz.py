# A set is a list of values that can be compared to other sets using opeartors such as
# intersection, difference, symmetric_difference, and union.

mydict = {"Mack": {"Age": 16, "Color": "Purple", "Sophomore":True}}
mydict.update({"Phin": {"Age": 15, "Color": "Red", "Sophomore":False}})
mydict.update({"Bob": {"Age": 19, "Color": "Maroon", "Sophomore":False}})

for key in mydict.keys():
    name = key
    age = mydict[key]["Age"]
    color = mydict[key]["Color"]
    if mydict[key]["Sophomore"]: sophomore = "is"
    if not mydict[key]["Sophomore"]: sophomore = "is not"
    print(f"{name} is {age} years old, his favorite color is {color}, and he {sophomore} a sophomore")

# This program fulfills the requirements because the dictionary 'mydict' holds 3 keys,
# houses four mixed types (int, string, bool, and another dict), and retrieves
# values when keys are given
