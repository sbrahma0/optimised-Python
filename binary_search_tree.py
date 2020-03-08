'''
The first number is the root, then the insertion is such that the left is smaller than the root and the right is larger than the root
like if we enter these numbers in sequenct - 4 2 8 5 10, then the tree looks like this
        4
      /   \
     2     8
          / \
         5   10 
'''
class Node:
    def __init__(self, data = None):
        self.data = data # Constructor
        self.right = None
        self.left = None

class binary_search_tree:
    def __init__(self): # Constructor
        self.root = None
    
    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert(data, self.root) # helper function which is gone insert the elements based on different comparisons
        
    def _insert(self, data, current_node):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert(data, current_node.left)
        
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert(data, current_node.right)
        
        else:
            print("The value is already present")
    
    def find(self,data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            return False
        return None
    
    def _find(self, data, current_node):
        if data > current_node.data and current_node.right:
            self._find(data, current_node.right)
        elif data < current_node.data and current_node.left:
            self._find(data, current_node.left)
        elif data == current_node.data:
            return True
    
bst = binary_search_tree()
bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)

print(bst.find(1))
