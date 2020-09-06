class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.mirror(root.left, root.right)
    
    def mirror(self, a, b):
        if a and b:
            return a.val == b.val and self.mirror(a.left, b.right) and self.mirror(a.right, b.left)
        return a is b
