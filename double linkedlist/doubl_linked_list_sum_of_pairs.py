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

    # This function delets the node which is given as an argument
    
    def delete_node(self, key):
        # Case 1 - If the node to be deleted is the only element in the list
        # Case 2 - If the list has 2 elements and the head is to be deleted
        # Case 3 - If the node to be deleted is anywhere except 1st, 2nd and last position
        # Case 4 - If the node to be deleted is the last node of the list
        
        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:
                # Case 1
                if cur.nest is None:
                    cur = None
                    self.head = None
                    return
                # Case 2
                else:
                    nxt = cur.nest
                    nxt.prev = None
                    cur.nest = None
                    cur = None
                    self.head = nxt
                    return
            elif cur.data == key:
                # Case 3
                if cur.nest:
                    nxt = cur.nest
                    pre = cur.prev
                    pre.nest = nxt
                    nxt.prev = pre
                    cur.nest = None
                    cur.prev = None
                    cur = None
                    return
                # Case 4 
                else:
                    #print('///',cur.data)
                    pre = cur.prev 
                    #print('---',pre.data)
                    pre.nest = None 
                    return 
            cur = cur.nest


#************
# This function takes the node as an arguement instead of taking the key of the node
    def delete_node_node(self, node):
        # Case 1 - If the node to be deleted is the only element in the list
        # Case 2 - If the list has 2 elements and the head is to be deleted
        # Case 3 - If the node to be deleted is anywhere except 1st, 2nd and last position
        # Case 4 - If the node to be deleted is the last node of the list
        
        cur = self.head
        while cur:
            if cur == node and cur == self.head:
                # Case 1
                if cur.nest is None:
                    cur = None
                    self.head = None
                    return
                # Case 2
                else:
                    nxt = cur.nest
                    nxt.prev = None
                    cur.nest = None
                    cur = None
                    self.head = nxt
                    return
            elif cur == node:
                # Case 3
                if cur.nest:
                    nxt = cur.nest
                    pre = cur.prev
                    pre.nest = nxt
                    nxt.prev = pre
                    cur.nest = None
                    cur.prev = None
                    cur = None
                    return
                # Case 4 
                else:
                    #print('///',cur.data)
                    pre = cur.prev 
                    #print('---',pre.data)
                    pre.nest = None 
                    return 
            cur = cur.nest
#*************
    
    def reverse_list(self):
        temp = None
        cur = self.head
        while cur:
            temp = cur.prev
            cur.prev = cur.nest
            cur.nest = temp
            cur = cur.prev # Here since the arrows of next and previous are switched, so the progression will be along the previous arrow instead of nest arrow
        #print('+++',temp.data, temp.prev.data)
        if temp:
            self.head = temp.prev
    # To remove a duplicate there are 2 ways:
    # 1 - Call the delete function by either passing the key of the node or modifying the delete function to take nodes as arguement instead of keys
    # 2 - Perform the delete operation in this function iteself, in that case it save from running another loop in the delete function
    # For 1 option 1 , it wont work becasue it will remove the fist instance of the repeating element and not the 2nd instance,
    # So its ggod to change the delete_node to a node accepting delete funtion
    def remove_duplicates(self):
        cur = self.head
        #print("pppppppppppppppp",cur.data)
        prev = cur.prev
        nxt  =cur.nest
        seen = {}
        while cur:
            if cur.data not in seen:
                seen[cur.data] = 1
                cur = cur.nest
            
            else:
                nxt = cur.nest
                self.delete_node_node(cur)
                cur = nxt
        
        #print(seen)
        
    def sum_of_pairs(self, sum_val):
        cur = self.head
        cur_nest = None
        pairs = []
        while cur:
            cur_nest = cur.nest
            while cur_nest:
                if cur.data + cur_nest.data == sum_val:
                    pairs.append('('+str(cur.data)+'+'+str(cur_nest.data)+')')
                cur_nest = cur_nest.nest
            cur = cur.nest
        return pairs
    
dlist = double_linked_list()
dlist.append(1)
dlist.append(2)
dlist.append(3)
dlist.prepend(0)
dlist.append(4)
dlist.append(5)
dlist.append(6)
dlist.print_list()
#dlist.delete_node(3)
print('**')
print(dlist.sum_of_pairs(0))
#dlist.print_list()
