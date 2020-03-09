'''
The first number is the root, then the insertion is such that the left is smaller than the root and the right is larger than the root
like if we enter these numbers in sequenct - 4 2 8 5 10, then the tree looks like this
        4
      /   \
     2     8
          / \
         5   10 
'''
# defining thwe quary class for adding and popping the node values in the list
class Queue(object):
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].data

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

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
    
    # This function is to calculate the height of the node
    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        
        return 1+max(left_height,right_height)
    
# This function is to perform level wise traversal of the tree.
    
    def levelorder_print(self, start):
        if start is None:
            return 

        queue = Queue()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + " "
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal
    
bst = binary_search_tree()
bst.insert(4)
bst.insert(2)
bst.insert(1)
bst.insert(3)
bst.insert(8)
bst.insert(5)
bst.insert(10)

# Finding the existance of a value in the tree
print(bst.find(1))
# Finding th eheight if a given node
print(bst.height(bst.root.right))
# Printinh the value of a node
print(bst.root.right.left.data)
# Level wise level_vise_traversal
print(bst.levelorder_print(bst.root))
        
