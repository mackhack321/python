def addEmployee():
    usr = "foo"
    print("Type 'done' to quit")
    while usr != "done":
        usr = input("Employee to add: ")
        if usr == "done": break
        employees.add(usr)

def reposEmployee():
    if len(employees) == 0:
        print("No employees to edit")
    else:
        print("Employees: ",", ".join(employees))
        employee = input("Employee to move: ")
        newpos = input("To what position? Associate, assistant manager, or manager? (as/am/m): ")
        if newpos == "as":
            managers.discard(employee)
            asst_managers.discard(employee)
            employees.add(employee)
        elif newpos == "am":
            if employee in managers:
                managers.remove(employee)
            asst_managers.add(employee)
        elif newpos == "m":
            if employee in asst_managers:
                asst_managers.remove(employee)
            managers.add(employee)

def listEmployees():
    print("Assistant Managers: ",", ".join(asst_managers))
    print("Managers: ",", ".join(managers))
    print("Associates: ",", ".join(employees - asst_managers - managers))
    input("Press enter to return to the menu...")

def menu():
    goodChoice = False
    choice = "foo"
    while goodChoice is False:
        print(
"""===== Employee Database =====
||    Add Employees - 1    ||
||    Move Employee - 2    ||
||      List All - 3       ||
||        Exit - 4         ||
=============================""")
        try:
            choice = int(input("Select an action: "))
            if choice == add: addEmployee()
            elif choice == promote: reposEmployee()
            elif choice == listall: listEmployees()
            elif choice == exit: break
        except ValueError:
            continue
            
## init sets ##
employees = set()
asst_managers = set()
managers = set()
## init menu constants ##
add = 1
promote = 2
listall = 3
exit = 4

menu()
