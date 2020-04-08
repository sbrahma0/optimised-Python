# Vertical traversing of a binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def vertical_order(root):
    if not root:
        return
    dic = {} # Stores the final output
    que = [] # Stores the generated nodes
    nodes = {} # stores the nodes with their levels
    que.append(root)
    nodes[root.data] = 0
    while que!= []:
        temp = []
        cur = que.pop(0)
        if cur:
            level = nodes[cur.data]
            if level not in dic:
                temp.append(cur.data)
                dic[level] = temp
            else:
                temp = dic.get(level)
                temp.append(cur.data)
            if cur.left:
                que.append(cur.left)
                nodes[cur.left.data] = nodes[cur.data]-1
            if cur.right:
                que.append(cur.right)
                nodes[cur.right.data] = nodes[cur.data]+1
    return dic
    
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
print(vertical_order(root))
