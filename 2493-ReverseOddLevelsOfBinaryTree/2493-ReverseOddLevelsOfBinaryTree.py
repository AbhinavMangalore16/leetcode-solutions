# Last updated: 3/31/2026, 9:31:38 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(ln, rn, lvl):
            if not (ln and rn):
                return 
            if not lvl%2:
                ln.val, rn.val = rn.val, ln.val
            helper(ln.left, rn.right, lvl+1)
            helper(ln.right, rn.left, lvl+1)
        helper(root.left, root.right, 0)
        return root
        