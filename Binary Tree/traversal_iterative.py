class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        left_right = []
        final = []
        
        if root:
            left_right.append(root)
            
        while left_right:
            node = left_right.pop()
            if node:
                final.append(node.val)
            
            if node.left:
                left_right.append(node.left)
            if node.right:
                left_right.append(node.right)
        
        final.reverse()        
        return final
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        final = []
        left = []
               
        while root or left:
            if root:
                left.append(root)
                root = root.left
            else:
                root = left.pop()
                final.append(root.val)
                root = root.right
        
        return final
