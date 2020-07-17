class a:
    def __init__(self):
        self.c1 = 1
    def method1(self):
        print("Name- ",self.c1)

class b(a):
    def __init__(self):
        self.c2 = 2
        a.__init__(self)
        #super().__init__()
        self.calling()
    
    def method1(self):
        print("Name- ",self.c2)

    def calling(self):
        self.method1()
        a.method1(self)
    
    
ob = b()
