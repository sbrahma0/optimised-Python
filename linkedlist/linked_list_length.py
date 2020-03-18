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

# To delete a node when the value/data of the node is given
    def delete_node(self, key):
        current_node = self.head
        prev_node = None
        
        if current_node and current_node.data == key:
            self.head = current_node.nest
            current_node = None
            return
        
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.nest
        
        if current_node is None:
            return
        
        prev_node.nest = current_node.nest
        current_node = None

# To delete a node with the given position
    
    def del_pos_node(self, pos):
        
        current_node = self.head
        prev_node = self.head
        i=0
        if pos == 0:
            self.head = current_node.nest
            current_node = None
            return
        
        while current_node and i < pos:
            prev_node = current_node
            current_node = current_node.nest
            i = i+1
        
        if current_node is None:
            return
        
        prev_node.nest = current_node.nest
        current_node = None
    
    # This is the iterative method to get the length of the linked_list
    def count_length(self):
        prev_node = None
        current_node = self.head
        count = 0
        
        while current_node:
            prev_node = current_node
            current_node = current_node.nest
            count = count+1
        
        return count
    
    # This is the recursive methd to get the length of the linked_list, here we need to give a starting node
    def count_length_recursion(self, node):
        if node is None:
            return 0
        return 1+self.count_length_recursion(node.nest)
    
llist = linked_list()
llist.append('a')
llist.append('b')
llist.append('c')
llist.append('d')
llist.insert_after_node(llist.head.nest,'e')
llist.printlist()
print("*******")
#llist.delete_node('a')
#llist.printlist()
#llist.del_pos_node(5)
#llist.printlist()
print("The length of the list in loop method- ",llist.count_length())
print("The length of the list in loop method- ",llist.count_length_recursion(llist.head))
