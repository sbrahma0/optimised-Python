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
    
    
    def swap_nodes(self, key1, key2):
        
        if key2 == key1:
            return
        
        previous1 = previous2 = None
        current_node1 = current_node2 = self.head
        
        # this condition is for the fact that id the entered arguement is an empty character
        while current_node1 and current_node1.data != key1:
            previous1 = current_node1
            current_node1 = current_node1.nest
        
        while current_node2 and current_node2.data != key2:
            previous2 = current_node2
            current_node2 = current_node2.nest
        
        #print(current_node1.data)
        #print(current_node2.data)
        # This is to check if either of the 2 nodes are not empty
        # This condition is to check ehether the arguement node given is in the list or not
        if current_node1 and current_node2:
            if previous1:
                previous1.nest = current_node2
            else:
                self.head = current_node2
            
            if previous2:
                previous2.nest = current_node1
            else:
                self.head = current_node1    
        

            current_node1.nest, current_node2.nest = current_node2.nest, current_node1.nest
    
    # This si helper function to better understand the reversing concept by providing printing at all stages
    def print_helper(self, node, name):
        if node is None:
            print(name + ": None")
        else:
            print(name + ":" + node.data)    
    
    
    
    # Reverse the linked list in iterative as well as recursive way
    # None -> a -> b -> e -> c -> d -> None
    # we want  None <- a <- b <- e <-c <- d <- None
    def reverse_iterative(self):
        prev = None
        cur = self.head
        
        while cur:
            nxt = cur.nest
            cur.nest = prev
            
            self.print_helper(prev, "PREV")
            self.print_helper(cur, "CUR")
            self.print_helper(nxt, "NXT")
            print("\n")
            
            prev = cur
            cur = nxt
        self.head = prev
    
    # Recursice way of reversing the linked list
    def reverse_recursive(self):
        
        def _reverse_recursive(cur, prev):
            
            if not cur :
                return prev
            
            nxt = cur.nest
            cur.nest = prev
            prev = cur 
            cur = nxt
            
            return _reverse_recursive(cur, prev)
        
        self.head = _reverse_recursive(cur=self.head, prev=None)
    
llist = linked_list()
llist.append('a')
llist.append('b')
llist.append('c')
llist.append('d')
llist.insert_after_node(llist.head.nest,'e')
#llist.printlist()
print("*******")
#llist.delete_node('a')
#llist.printlist()
#llist.del_pos_node(5)
#llist.printlist()
#print("The length of the list in loop method- ",llist.count_length())
#print("The length of the list in loop method- ",llist.count_length_recursion(llist.head))
#llist.swap_nodes('d','a')
#llist.reverse_iterative()
#llist.printlist()
print('///////////////')
llist.reverse_recursive()
llist.printlist()
