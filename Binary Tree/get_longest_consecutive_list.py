# Find out the longest consecutive sequence in a tree (Binary)
class node: 
    def __init__(self, value): 
        self.val = value  
        self.left = self.right = None

# This function is for initiating with the root node
def longestConsecutive(root):
    if root is None:
        return 0
    
    longest_length = [0]
    reccurrng(root, 0, root.val, longest_length)
    
    return longest_length[0]

# This is the recurring funtion which gets called for left and right branches
def reccurrng(root, current_length, expected, longest_length):
    if root is None:
        return
    
    if root.val == expected:
        current_length += 1
    else:
        current_length = 1
    
    longest_length[0] = max(longest_length[0],current_length)
    # The expected value is the next vale of the previous value since it is for the consecutive sequence
    reccurrng(root.left, current_length, root.val + 1, longest_length) 
    reccurrng(root.right, current_length, root.val + 1, longest_length)
    
  
root = node(1)
root.left = node(6)
root.right = node(2)
root.right.left = node(5)
root.right.right = node(3)
root.right.right.left = node(4)
print(longestConsecutive(root))
