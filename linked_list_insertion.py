class Node:
    def __init__(self, data):
        self.data = data
        self.nest = None
    

class linked_list:
    def __init__(self):
        self.head = None
    
    def printlist(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.nest
    
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.nest:
            last_node = last_node.nest
            
        last_node.nest = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        
        new_node.nest = self.head
        self.head = new_node
        
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Node not present")
            return
        
        new_node = Node(data)
        new_node.nest = prev_node.nest
        prev_node.nest = new_node
        
        

llist = linked_list()
llist.append('a')
llist.append('b')
llist.append('c')
llist.append('d')
llist.insert_after_node(llist.head.nest,'e')
llist.printlist()
