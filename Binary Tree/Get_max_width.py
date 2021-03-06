class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def height(root):
    
    if not root:
        return 0
    else:
        #print(root.val)
        left = height(root.left)
        right = height(root.right)
        
        
        if left>right:
            return left+1
        else:
            return right+1


def getMaxWidth(root): # acceps the head of a binary tree
    max_width = 0
    levels = height(root)
    #print(levels)
    for lev in range(0,levels):
        width = getWidth(root, lev)
        if width>max_width:
            max_width = width
    
    return max_width

def getWidth(root, level):
    if not root:
        return 0
    if level == 0:
        return 1
    else:
        return (getWidth(root.left, level-1)+getWidth(root.right, level-1))

# The above mentioned method is of O(n^2)
# Below is O(n)
# Comment all the functions above this, except the class node
'''
def getMaxWidth(root): # acceps the head of a binary tree
    if root is None:
        return 0
    
    maxwidth = 0
    q = []
    q.insert(0,root)
    while q != []:
        count = len(q)
        maxwidth = max(count, maxwidth)
        
        while count != 0:
            count -= 1
            temp = q[-1]
            q.pop()
            if temp.left:
                q.insert(0, temp.left)
            if temp.right:
                q.insert(0, temp.right)
    
    return maxwidth
'''

root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.left.left = Node(8)
root.left.right = Node(6)
root.right.right = Node(7)
root.right.right.left = Node(11)
root.right.right.right = Node(12)
root.left.right.left = Node(9)
root.left.right.right = Node(10)

print(getMaxWidth(root))
