# Last updated: 3/31/2026, 9:38:39 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        lt = self.lowestCommonAncestor(root.left, p, q)
        rt = self.lowestCommonAncestor(root.right, p, q)
        if lt and rt:
            return root
        elif lt and not rt:
            return lt
        elif not lt and rt:
            return rt
        else:
            return None
        