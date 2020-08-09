
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class bst:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root == None:
            self.root = node(data)
            return
        self._insert(data, self.root)
    
    def _insert(self, data, current):
        if data<current.data:
            if current.left == None:
                current.left = node(data)
            else:
                self._insert(data, current.left)
        
        elif data>current.data:
            if current.right == None:
                current.right = node(data)
            else:
                self._insert(data, current.right)
        else:
            print("This element exists")

def lot(root):
    if not root:
        return 
    
    q = []
    traversed = []
    q.append(root)
    while (len(q)>0):
        count = len(q) # detrmine the level we are tracversing
        while count>0:
            cur = q[0]
            q.pop(0)
            if cur.data==root.data:
                print(cur.data)
            else:
                print(cur.data,end=" ")
            
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
            
            count -=1
        print()
# Vertical order traversal
def vot(root):
    q=[] # Stores the nodes as they appear
    dic = {} # Stores the final answer with levels and sets
    nodes = {} # Stores the nodes with levels
    
    q.append(root)
    nodes[root.data] = 0
    
    while q!=[]:
        temp = []
        cur = q.pop(0)
        if cur:
            level = nodes[cur.data]
            if level not in dic:
                temp.append(cur.data)
                dic[level] = temp
            else:
                temp = dic.get(level)
                temp.append(cur.data)
            if cur.left:
                q.append(cur.left)
                nodes[cur.left.data] = nodes[cur.data]-1
            if cur.right:
                q.append(cur.right)
                nodes[cur.right.data] = nodes[cur.data]+1
    
    return dic
bst1 = bst()
bst1.insert(4)
bst1.insert(2)
bst1.insert(8)
bst1.insert(5)
bst1.insert(10)
bst1.insert(1)
bst1.insert(3)
bst1.insert(9)
bst1.insert(11)
lot(bst1.root)
print("----")
print(bst1.root.right.right.data)
print(vot(bst1.root))

'''
class binary_tree:
    def __init__(self, root):
        self.root = node(root)
    
    def traversal_choice(self, traversal):
        if traversal == "PreOrder":
            return self.pre_order(self.root,'')
        if traversal == "InOrder":
            return self.in_order(self.root,'')
        if traversal == "PostOrder":
            return self.post_order(self.root,'')
        
        return
    
    # root->left->right
    def pre_order(self, start, traversal):
        
        if start:
            traversal = traversal + str(start.data)
            traversal = self.pre_order(start.left,traversal)
            traversal = self.pre_order(start.right,traversal)
        return traversal
        
    # left->root->right
    def in_order(self, start, traversal):
        
        if start:
            traversal = self.in_order(start.left,traversal)
            traversal = traversal + str(start.data)
            traversal = self.in_order(start.right,traversal)
        return traversal
    
b1 = binary_tree(1)
b1.root.left = node(2)
b1.root.right = node(3)       
b1.root.left.left = node(4)
b1.root.left.right = node(5)
b1.root.right.left = node(6)
b1.root.right.right = node(7)

print(b1.traversal_choice("InOrder"))
'''
