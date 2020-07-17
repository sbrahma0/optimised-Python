# Single inheritance
class person:
    def __init__(self,name):
        self.name = name
    
    def display_name(self):
        print("Name- ",self.name,"\n")

class employee(person):
    def __init__(self, name, id):
        self.id = id
        person.__init__(self,name)
    
    def display_id(self):
        print("ID- ",self.id)

a = employee("sayan",10)
a.display_id()
a.display_name()

# Multiple inheritance
'''

class base1:
    def __init__(self):
        self.st1 = "String 1"
        print("Base1")

class base2:
    def __init__(self):
        self.st2 = "String 2"
        print("Base2")

class derived(base1, base2):
    def __init__(self):
        print("Derived")
        base1.__init__(self)
        base2.__init__(self)
    def pr(self): # st1 and st2 cannot be accessed outside a function
        print(self.st1)
        print(self.st2)

a = derived()
a.pr()
