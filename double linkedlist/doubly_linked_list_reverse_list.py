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
#dlist.delete_node(3)
print('**')
dlist.reverse_list()
dlist.print_list()
