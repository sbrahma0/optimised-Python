# Multilevel inheritance

class parent:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        print("Name- ",self.name)

class child(parent):
    def __init__(self, name, age):
        self.age = age
        parent.__init__(self, name)
    def get_age(self):
        print("Age- ",self.age)

class grand_child(child):
    def __init__(self, name, age, address):
        self.address = address
        child.__init__(self, name, age)
    def get_address(self):
        print("Address- ",self.address)

a = grand_child('Sayan', 15, 'Park')
a.get_name()
a.get_age()
a.get_address()
