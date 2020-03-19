# Double lined list

class node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.nest = None

class double_linked_list:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.nest:
                cur = cur.nest
            cur.nest = new_node
            new_node.prev = cur
            

    def prepend(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.nest = self.head
            self.head = new_node
    
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.nest

dlist = double_linked_list()
dlist.append(1)
dlist.append(2)
dlist.append(3)
dlist.prepend(0)
dlist.print_list()
