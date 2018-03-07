## init sets ##
employees = set()
asst_managers = set()
managers = set()
## init menu constants ##
add = 1
promote = 2
listall = 3
exit = 4

def addEmployee():
    usr = "foo"
    print("Type 'done' to quit")
    while usr != "done":
        usr = input("Employee to add: ")
        if usr == "done": break
        employees.add(usr)

def promoteEmployee():
    if len(employees) == 0:
        print("No employees to promote")
    else:
        print("Employees: ",", ".join(employees))
        employee = input("Employee to promote: ")
        newpos = input("To what position? Assistant manager or manager? (a/m): ")
        if newpos == "a":
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
    print("Everyone Else: ",", ".join(employees - asst_managers - managers))

def menu():
    goodChoice = False
    choice = "foo"
    while goodChoice is False:
        print(
"""===== Employee Database =====
||    Add Employees - 1    ||
||   Promote Employee - 2  ||
||      List All - 3       ||
||        Exit - 4         ||
=============================""")
        try:
            choice = int(input("Select an action: "))
            if choice == add: addEmployee()
            elif choice == promote: promoteEmployee()
            elif choice == listall: listEmployees()
            elif choice == exit: break
        except ValueError:
            continue

menu()
