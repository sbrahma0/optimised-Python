# Binary tree traversal
# Preorder, inorder and post inorder
'''
        1
      /   \
     2     3
    / \   / \
   4   5 6   7

Trying to depict this sequence. 1. Make this tree and print the elements of the tree
This is also an example of object oriented programing
'''
# This class node creates 2 spots for each node
class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

# This class initialises th programe with assigning the root
class Binary_tree(object):
    def __init__(self, root):
        self.root = Node(root)

    

    def Pre_order(self, start, traversal):
        # root->left->right
        if start:
            traversal = traversal + str(start.value)+' '
            traversal = self.Pre_order(start.left, traversal)
            traversal = self.Pre_order(start.right, traversal)
    
        return traversal
    
    
    def In_order(self, start, traversal):
        # left->root->right
        if start:
            traversal = self.In_order(start.left, traversal)
            traversal = traversal + str(start.value)+' '
            traversal = self.In_order(start.right, traversal)
    
        return traversal
    
    def Post_order(self, start, traversal):
        # left->right->root
        if start:
            traversal = self.Post_order(start.left, traversal)
            traversal = self.Post_order(start.right, traversal)
            traversal = traversal + str(start.value)+' '
    
        return traversal
    
    def print_tree(self, traversal_type):
        if traversal_type == 'Pre_order':
            return self.Pre_order(tree.root,'')
        
        elif traversal_type == 'In_order':
            return self.In_order(tree.root,'')
        
        elif traversal_type == 'Post_order':
            return self.Post_order(tree.root,'')
        
        else:
            return False
    


tree = Binary_tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

#print(tree.print_tree('Pre_order'))
#print(tree.print_tree('In_order'))
print(tree.print_tree('Post_order'))

'''
Pre_order output should be - 1 2 4 5 3 6 7
In_order output should be - 4 2 5 1 6 3 7
Post_order output shoukd be - 4 5 2 6 7 3 1
'''
