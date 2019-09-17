import pickle as p

class Account(object):
    def __init__(self, name, age, num):
        self.balance = 0.00
        self.name = name
        self.age = age
        self.num = num
    
    def withdraw(self, amount):
        if (self.balance > amount):
            self.balance -= amount
        else: print("Insufficient funds.")
    
    def deposit(self, amount):
        self.balance += amount

    def write(self):
        data = {"name":self.name, "balance":self.balance, "age":self.age, "num":self.num}
        p.dump(data,open(f"{self.name}.secret","wb"))

    def __str__(self):
        return f"{self.name}: ${self.balance}, {self.age} year(s) old, account number {self.num}"

    def load(self):
        try:
            data = p.load(open(f"{self.name}.secret","rb"))
            if int(data["num"]) == self.num and data["name"] == self.name:
                self.balance = data["balance"]
                self.name = data["name"]
                self.age = data["age"]
                print("Imported data")
        except: pass

name = input("Enter name :: ")
age = int(input("Enter age :: "))
num = int(input("Enter account number :: "))

acct = Account(name,age,num)
acct.load()

VIEW = "1"
WITHDRAW = "2"
DEPOSIT = "3"
SAVE = "4"

while 1:
    print("1: View Balance")
    print("2: Withdraw")
    print("3: Deposit")
    print("4: Save and Quit")
    choice = input("Enter choice :: ")

    if choice == VIEW:
        print(acct)
    elif choice == WITHDRAW:
        amt = float(input("How much? :: "))
        acct.withdraw(amt)
    elif choice == DEPOSIT:
        amt = float(input("How much? :: "))
        acct.deposit(amt)
    elif choice == SAVE:
        acct.write()
        print("Goodbye")
        break
