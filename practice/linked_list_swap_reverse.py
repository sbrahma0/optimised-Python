class Node:
    def __init__(self,data):
        self.value = data
        self.nest = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        
        current = self.head
        while current.nest:
            current = current.nest
        
        current.nest = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        
        new_node.nest = self.head
        self.head = new_node
    
    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.nest
        
    # swap, reverse
    def swap(self, data1,data2):
        current1 = current2 = self.head
        previous1 = previous2 = None
        
        while(current1):
            if current1.value == data1:
                break
            previous1 = current1
            current1 = current1.nest
        
        while(current2):
            if current2.value == data2:
                break
            previous2 = current2
            current2 = current2.nest
        
        if current2 and current1:
            if previous1:
                previous1.nest = current2
            else:
                self.head = current2
            
            if previous2:
                previous2.nest = current1
            else:
                self.head = current1
            
            current1.nest, current2.nest = current2.nest, current1.nest
    
    
    def reverse_iterative(self):
        previous = None
        if self.head:
            current = self.head
        
        while current:
            next = current.nest
            current.nest = previous
            previous = current
            current = next
        
        self.head = previous
    
    def reverse_recusrive(self):
        def _reverse_recusrive(cur, pre):
            if not cur :
                return pre
            next = cur.nest
            cur.nest = pre
            pre = cur
            cur = next
            return _reverse_recusrive(cur, pre)
        
        self.head = _reverse_recusrive(self.head, None)
    
l1 = LinkedList()
l1.append(5)
l1.append(7)
l1.prepend(3)
l1.append(9)
l1.print_list()
l1.swap(3,9)
print("SWAPPWD")
l1.print_list()

print("REVERSED")
l1.reverse_iterative()
l1.print_list()

print("REVERSED recursive")
l1.reverse_recusrive()
l1.print_list()
