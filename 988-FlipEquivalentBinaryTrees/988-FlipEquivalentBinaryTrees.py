# Last updated: 3/31/2026, 9:36:07 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def helper(r1,r2):
            if not r1 and not r2:
                return True
            if not r1 or not r2 or r1.val!=r2.val:
                return False
            return (helper(r1.left, r2.left) or helper(r1.left, r2.right)) and (helper(r1.right, r2.right) or helper(r1.right, r2.left))
        return helper(root1, root2)