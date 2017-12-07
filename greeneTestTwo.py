"""
Write Python code that asks the user a question,
takes at least two user inputs, operates on those inputs,
and outputs something back to the user based on the operation.
"""

print("Greetings, user!  This is an average grade calculator.\n")
grades = []
more = "bob"
while more == "bob":
    try:
        grades.append(float(input("Give a percentage grade to add to the list, but do not add the percent sign:\n")))
    except ValueError:
        print("ERROR: Invalid Data Type.  Grades should either be an integer or a float.  Do not include the percent sign")
        
    while more != "y" and more != "n":
        more = str.lower(input("Would you like to add another grade? y or n: "))
    if more == "y":
        more = "bob"
    elif more == "n":
        try:
            avg = round(sum(grades)/len(grades), 0)
        except ZeroDivisionError:
            print("ERROR: No Grades Found")
            break
        
        print("Grades to be Averaged:")
        for i in grades:
            print("{}%".format(i))
        print("The rounded average of the grades given is: {}%".format(int(avg)))
        if len(grades) == 1:
            print("...for this program to be of any sort of use, you must give at least two grades.")
    
