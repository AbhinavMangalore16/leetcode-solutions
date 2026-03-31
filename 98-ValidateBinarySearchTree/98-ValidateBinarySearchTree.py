# Last updated: 3/31/2026, 9:40:07 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(root, float('-inf'), float('inf'))
    def valid(self, root: Optional[TreeNode], min_range: float, max_range: float)->bool:
        if not root:
            return True
        if min_range<root.val<max_range:
            left = self.valid(root.left, min_range, root.val)
            right = self.valid(root.right, root.val, max_range)
            return left and right
        else:
            return False
    