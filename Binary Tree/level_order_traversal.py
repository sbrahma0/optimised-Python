# Vertical traversing of a binary tree
class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
'''
# This will give the output in 1 line
# This is using a loop
def level_order_traversal(root):
    if not root:
        return
    q=[]
    traversed = []
    q.append(root)
    while q != []:
        cur = q[0]
        #print(cur,'****')
        q.pop(0)
        traversed.append(cur.val)
        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)
    return traversed
'''
# This is to print the nodes in different levels
# This is using loop
def level_order_traversal(root):
    if not root:
        return
    q=[]
    traversed = []
    q.append(root)
    while len(q)>0:
        count = len(q)
        while count>0:
            cur = q[0]
            #print(cur,'****')
            q.pop(0)
            print(cur.val,end=" ")
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
            count -= 1
        
        print()


root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.right = Node(8)
root.right.right.left = Node(6)
root.right.right.left.left = Node(9)
root.right.right.left.right = Node(10)
root.right.right.right = Node(7)
root.right.right.right.left = Node(11)
root.right.right.right.right = Node(12)
level_order_traversal(root)
