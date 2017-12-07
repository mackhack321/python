class apple:
    """A simple example class"""
    i = 12345

    def f():
        return 'hello world'
    def __init__(self):
        print("FOOBAR!")
        print(str(self.i))

class dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

class tricks:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

class name:

    global ageList
    ageList = []

    def __init__(self,name):
        self.name = name
        print("Hello, {}.".format(name))
        
    def age(age):
        ageList.append(age)
        return ageList
