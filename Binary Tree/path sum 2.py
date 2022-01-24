# https://leetcode.com/problems/path-sum-ii/

#You are given a sum and BST, find the paths which give that sum


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        if root is None:
            return []
        
        return self.helper(root, targetSum, [],[])
    
    def helper(self, root, target_sum, current, result):
        
        if root.left is None and root.right is None:
            if target_sum-root.val == 0:
                result.append(current+[root.val])
        
        if root.left:
            self.helper(root.left, target_sum-root.val,current+[root.val],result)
        if root.right:
            self.helper(root.right, target_sum-root.val,current+[root.val],result)
        
        return result
