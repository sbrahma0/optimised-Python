# Binary tree to circular Doubly linked list - via inorder traversal, covers BST to sorted DLL too(Inplace) 
# please refer to bt_to_dll.py too

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class btt_to_dll:
    def __init__(self):
        self.prev = None
        self.head = None
    
    def convert(self,node):
        if node is None:
            return
        
        self.convert(node.left)
        
        #print("left nood",node.data)
        
        if self.head == None:
            self.head = node
        else:
            self.prev.right = node
            node.left = self.prev
        self.prev = node
        
        #print("root root",node.data)
        
        self.convert(node.right)
        
        #print("right root",node.data)
        #print("prev", self.prev.data)
        if self.prev.right == None: # this is to convert it into cyclic DLL
            self.prev.right = self.head
            self.head.left = self.prev
    
    def print_dll(self):
        node = self.head
        while node is not None:
            print(node.data, end=" ")
            node = node.right
            if node == self.head: # To check that we have a cyclice dll
                print(node.data)
                print("Cycle")
                break

# Let us create the tree as 
# shown in above diagram
root = Node(10)
root.left = Node(12)
root.right = Node(15)
root.left.left = Node(25)
root.left.right = Node(30)
root.right.left = Node(36)
root.right.right = Node(38)

btttodll = btt_to_dll()
btttodll.convert(root)
btttodll.print_dll()



