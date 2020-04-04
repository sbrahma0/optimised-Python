# Find out the longest path in a tree (Binary)

class node:
  def __init__(self, value):
    self.val = value
    self.left = None
    self.right = None

def get_list(root):
    if root is None:
        return []
    right = []
    left = []
    right = [root.val] + get_list(root.right)
    left = [root.val] + get_list(root.left)
    return get_max(right, left)
    
def get_max(list1, list2):
    if len(list2)>len(list1):
        return(list2)
    else:
        return(list1)


root = node('a')
root.left = node('b')
root.right = node('c')
root.right.left = node('d')
root.right.right = node('e')
root.right.right.left = node('f')

print(get_list(root))
