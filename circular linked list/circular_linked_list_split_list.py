# Circular linked list is like  a -> b -> c -> d -> e -> a So instead of the last node pointing towards none it points to the head node


class node:
    def __init__(self,data):
        self.data = data
        self.nest = None

class circular_linked_list:
    def __init__(self):
        self.head = None
    
    def prepend(self, data):
        if not self.head: # If the list is empty
            self.head = node(data)
            self.head.nest = self.head
        else: # if the lsit is not empty
            new_node = node(data)
            new_node.nest = self.head
            current_node = self.head
            while current_node.nest != self.head:
                current_node = current_node.nest
            current_node.nest = new_node
            self.head = new_node
        pass
    
    def append(self, data):
        if not self.head: # If the list is empty
            self.head = node(data)
            self.head.nest = self.head
        else:             # If the lsit is not empty
            new_node = node(data)
            current_node = self.head
            while current_node.nest != self.head:
                current_node = current_node.nest
            current_node.nest = new_node
            new_node.nest = self.head
    
    def print_list(self):
        current_node = self.head
        while current_node.nest != self.head:
            print(current_node.data)
            current_node = current_node.nest
        print(current_node.data)

    def remove_node(self, node_key):
        # If the key passed is equal to the head node, then these steps
        if self.head.data == node_key:
            current_node = self.head
            while current_node.nest != self.head:
                current_node = current_node.nest
            current_node.nest = self.head.nest
            self.head = self.head.nest
        else: 
            current_node = self.head
            prevous_node = None
            while current_node.nest != self.head:
                prevous_node = current_node
                current_node = current_node.nest
                if current_node.data == node_key:
                    prevous_node.nest = current_node.nest
                    current_node = current_node.nest # since the current node is not to be considered so the current node is moved forward by 1 more step
    
    def length_of_list(self):
        current_node = self.head
        count = 1 # This is to start the count from 1 instead of 0
        while current_node.nest != self.head:
            count += 1
            current_node = current_node.nest
        return count
    
    # This splits the list in 2 pivoting the mid way, so even distribution when 
    def split(self):
        if self.length_of_list() == 0:
            return
        if self.length_of_list() == 1:
            return self.head
        
        mid = self.length_of_list()//2
        prevous_node = None
        current_node = self.head
        count = 1
        new_list = circular_linked_list()
        while count <= mid and current_node:
            prevous_node = current_node
            current_node = current_node.nest
            count += 1
        prevous_node.nest = self.head
        
        #print('******',current_node.data, self.head.data)
        
        while current_node != self.head:
            new_list.append(current_node.data)
            current_node = current_node.nest
        #new_list.append(current_node.data)
        print("New List")
        new_list.print_list()
        print('end')

llist = circular_linked_list()
llist.append('a')
llist.append('b')
llist.append('c')
llist.append('d')
llist.append('e')
llist.append('f')
llist.print_list()
#llist.remove_node('d')
print('*****')
#print(llist.length_of_list())
llist.split()
print("old list splitted")
llist.print_list()
