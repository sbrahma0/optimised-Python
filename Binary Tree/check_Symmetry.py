# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # iteration
        
        # Recursion
        if not root:
            return True
        #return self.mirror(root.left, root.right)
        return self.mirror2(root)
    
        
    
    def mirror(self, a, b):
        if a and b:
            return a.val == b.val and self.mirror(a.left, b.right) and self.mirror(a.right, b.left)
        return a is b
    
    def mirror2(self,root): # Iteration
        layer_elements=[]
        node_config = []
        current_level = 0
        
        node_config.append((root,0))
        while node_config:
            leaf,level = node_config.pop(0)
            if current_level != level:
                current_level = level
                if layer_elements == layer_elements[::-1]:
                    layer_elements = []
                else:
                    return False
            
            if leaf.left:
                layer_elements.append(leaf.left.val)
                node_config.append((leaf.left, level+1))
            else:
                layer_elements.append(None)
            
            if leaf.right:
                layer_elements.append(leaf.right.val)
                node_config.append((leaf.right, level+1))
            else:
                layer_elements.append(None)
        
        return True
                    
            
