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
    

    def merge_sorted_list(self, llist):
        # here there will be 3 pointers, 1 for each heads to start with and 1 pointing towards the smallest among both of them
        p = self.head
        q = llist.head
        s = None
        
        if not p:
            return q
        if not q:
            return p
        
        if p and q:
            if p.data <= q.data:
                s = p
                p = p.nest
            else:
                s = q
                q = q.nest
            
            new_head = s
        
        # The above if condition and the new head assignment is for the 1st dtep
        while p and q:
            if p.data <= q.data:
                s.nest = p
                s = p
                p = s.nest
            else:
                s.nest = q
                s = q
                q = s.nest
        
        # It is a kind of last step i.e., if any of the list already reaches to the last node then since the lists are sorted, 
        #the s pointer can be directed to next node of then unfinished list.
        if not p:
            s.nest = q
        if not q:
            s.nest = p
        
        return new_head
        
    # This function is to remove duplicates by keeping the repeating elements in the 1st time position, this will also have an introduction of the dictionary
    def remove_duplicates(self):
        cur = self.head
        prev = None
        dup_values = {}
        
        while cur:
            if cur.data in dup_values:
                #delete the node
                prev.nest = cur.nest
                cur = None
            
            else:
                dup_values[cur.data] = 1
                prev = cur
            cur = prev.nest # So here we do not do cur.nest because if the node is in the dup dict, then the previous node will come into play and 
                            #the current node will be deleted
    
    # This function is to give the data of the node whise position has been given from the last node
    def nth_node_from_last_method1(self, pos):
        # get the length of the list
        length = self.count_length()
        cur = self.head
        while cur:
            if length == pos:
                print(cur.data)
                return cur.data
            
            length = length-1
            cur = cur.nest
        
        return
    
    def nth_node_from_last_method2(self, pos):
        p = self.head
        q = self.head
        
        if pos == self.count_length():
            return self.head.data
        count = 0
        while q and count < pos:
            q = q.nest
            count = count + 1
        if not q:
            print ("The entered node is out of bound")
            return
        
        while p and q:
            p = p.nest
            q = q.nest
        
        return p.data
            
    # This function gives the number of occurances of the element we've given as the arguement
    def count_occurances(self, data):
        count = 0
        cur = self.head
        while cur:
            if cur.data == data:
                count = count + 1
            cur = cur.nest
        
        return count
    
    # This is the recursive version of the previous function
    def count_occurances_recursion(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurances_recursion(node.nest, data)
        else:
            return self.count_occurances_recursion(node.nest, data)
        
    # To rotate a linked list
    # https://youtu.be/s9cEFnn-Y5Q?list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV
    
    def rotate_linked_list(self, pivot):
        if pivot <= 0:
            return
        p, q = self.head, self.head
        count = 1
        if pivot > self.count_length():
            return
        else:
            while p and q and count < pivot:
                p = p.nest
                q = q.nest
                count = count + 1
        
        print('///////////',p.data,q.data)    
        while q.nest:
            q = q.nest
        q.nest = self.head
        self.head = p.nest
        p.nest = None
        #print('///////////',p.data,q.data,q.nest.data,p.nest.data,self.head.data)
    
    # Palindrome function
    def Palindrome_method1(self):
        s = ""
        p = self.head
        while p:
            s += p.data
            p = p.nest
        return s == s[::-1] #This line checks whether the string is the same as original when reversed
    
    # Method 2 is the implementation of the stack i.e., a list with appned and pop features
    def Palindrome_method2(self):
        
        s=[]
        p = self.head
        while p:
            s.append(p.data)
            p = p.nest
        p = self.head
        while p:
            data = s.pop()
            if data != p.data:
                return False
            p = p.nest
        return True
    #Method 3 To perform the palindrome
    def Palindrome_method3(self):
        i = self.count_length()
        prev = []
        count = 0
        if i%2 == 0:
            limit = i//2
        else:
            limit = i//2+1
        
        p = q = self.head
        # This step is done to append all the elements of the linkedlist to a list
        while q.nest:
            prev.append(q.data)
            q = q.nest
        #now the elemenst from the list is appended from the last element i.e.m why we write -count
        while count <= limit and p:
            if prev[-count] != p.data:
                return False
            p = p.nest
            count += 1
        return True
        
        
llist1 = linked_list()
llist1.append('r')
llist1.append('a')
llist1.append('d')
llist1.append('a')
llist1.append('r')

llist1.printlist()
print('**********')
#llist1.remove_duplicates()
#llist1.printlist()
llist2 = linked_list()
llist2.append('a')
llist2.append('b')
llist2.append('b')
llist2.append('a')
#llist2.append('e')
#print(llist2.nth_node_from_last_method2(1))
#print(llist1.count_occurances('4'))
#print('***',llist1.count_occurances_recursion(llist1.head,'4'))
#llist1.rotate_linked_list(5)
#llist1.printlist()
print(llist1.Palindrome_method3())
print(llist2.Palindrome_method3())
