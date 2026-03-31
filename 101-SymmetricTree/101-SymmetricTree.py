# Last updated: 3/31/2026, 9:40:04 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def recur(s1: Optional[TreeNode], s2:Optional[TreeNode])->bool:
            if not s1 and not s2:
                return True
            elif not s1 or not s2:
                return False
            else:
                return s1.val==s2.val and recur(s1.left, s2.right) and recur(s1.right, s2.left)
        return recur(root,root)
