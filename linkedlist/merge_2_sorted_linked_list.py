# Merging 2 sorted linked listes
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

# This is the function which accepts 2 linked list heads and returns the head of the new merged list
# Recurreing approach
def merge(head1, head2):
    
    current = None
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    if head1.data <= head2.data:
        current = head1
        current.nest = merge(head1.nest, head2)
    else:
        current = head2
        current.nest = merge(head2.nest, head1)
    
    return current
'''
# This is the function which accepts 2 linked list and returns the head of the new merged list
# Loop approach
def merge(llist1, llist2):
    cur1 = llist1.head
    cur2 = llist2.head
    mergerd = linked_list()
    
    if not cur1:
        return llist2.head
    if not cur2:
        return llist1.head
    
    if cur1 and cur2:
        if cur2.data<=cur1.data:
            mergerd.append(cur2.data)
            cur2 = cur2.nest
        else:
            mergerd.append(cur1.data)
            cur1 = cur1.nest
        
    
    # this loop should continue untill either of the 2 gets fully esplored
    while cur2 and cur1:
        if cur1.data<=cur2.data:
            mergerd.append(cur1.data)
            cur1 = cur1.nest
        else:
            mergerd.append(cur2.data)
            cur2 = cur2.nest
    
    # After the previous loop 1 of the list gets traversed completely, so we need to traverse the remaining list
    
    while cur1:
        mergerd.append(cur1.data)
        cur1 = cur1.nest
    while cur2:
        mergerd.append(cur2.data)
        cur2 = cur2.nest
    
    return mergerd.head
'''   

llist1 = linked_list()
llist1.append('1')
llist1.append('5')
llist1.append('7')
llist1.append('9')
llist1.append('10')


llist2 = linked_list()
llist2.append('2')
llist2.append('3')
llist2.append('4')
llist2.append('6')
llist2.append('8')

llist3 = linked_list()
llist3.head = merge(llist1.head, llist2.head)
# llist3.head = merge(llist1, llist2) Use this if we are calling the loop approach
llist3.printlist()
