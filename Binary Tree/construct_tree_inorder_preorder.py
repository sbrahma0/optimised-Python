# Q link- https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Solution 1 - not optimal, best for understanding

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def rec(inorder, preorder):
            # Base condition
            if not preorder or not inorder: # since the lists will get smaller and smaller
                return
            
            
            root = TreeNode(preorder.pop(0))
            #print(root.val)
            mid = inorder.index(root.val)
            
            root.left = rec(inorder[:mid],preorder)
            root.right = rec(inorder[mid+1:],preorder)
            
            return root
        
        return rec(inorder, preorder)
      
# Solution 2 - Optimal
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        mapper = {}
        for index, value in enumerate(inorder):
            mapper[value] = index
        
        preorder = preorder[::-1]
        def rec(low, high):
            # Base condition
            if low<=high and len(preorder)!=0: # since the lists will get smaller and smaller
                
                root_val = preorder.pop()
                mid = mapper[root_val]
                root = TreeNode(root_val)
                root.left = rec(low, mid-1)
                root.right = rec(mid+1,high)
            
            
                return root
        
        return rec(0, len(inorder)-1)
