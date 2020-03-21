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
    
    # add_node_after and add_node_before functions are written without append and prepend function dependence
    def add_node_after(self, key, new_node):
        cur = self.head
        while cur:
            if cur.data == key:
                new_node = node(new_node)
                temp = cur.nest
                cur.nest = new_node
                new_node.prev = cur
                new_node.nest = temp
                if temp:
                    temp.prev = new_node
            cur = cur.nest
    
    def add_node_before(self, key, new_node):
        if key == self.head.data:
            new_node = node(new_node)
            self.head.prev = new_node
            new_node.nest = self.head
            self.head = new_node
        else:
            prev = None
            cur = self.head
            while cur:
                if cur.data == key:
                    new_node = node(new_node)
                    new_node.nest = cur
                    new_node.prev = prev
                    prev.nest = new_node
                    cur.prev = new_node
                prev = cur
                cur = cur.nest

    
dlist = double_linked_list()
dlist.append(1)
dlist.append(2)
dlist.append(3)
dlist.prepend(0)
#dlist.print_list()
print('**')
dlist.add_node_after(2,5)
dlist.add_node_before(0,9)
dlist.add_node_before(3,6)
dlist.print_list()
