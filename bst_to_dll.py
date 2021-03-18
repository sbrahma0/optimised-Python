# https://www.geeksforgeeks.org/convert-given-binary-tree-doubly-linked-list-set-3/
# Binary tree to Doubly linked list - via inorder traversal, covers BST to sorted DLL too(Inplace)
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
        
        if self.head == None:
            self.head = node
        else:
            self.prev.right = node
            node.left = self.prev
        self.prev = node
        
        self.convert(node.right)
        
        return self.head
    
    def print_dll(self):
        node = self.head
        while node is not None:
            print(node.data, end=" ")
            node = node.right

# Let us create the tree as 
# shown in above diagram
root = Node(10)
root.left = Node(12)
root.right = Node(15)
root.left.left = Node(25)
root.left.right = Node(30)
root.right.left = Node(36)

btttodll = btt_to_dll()
btttodll.convert(root)
btttodll.print_dll()



