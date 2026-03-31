# Last updated: 3/31/2026, 9:40:09 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lis = []
        def helper(root: Optional[TreeNode], lis: List[int]):
            if (root is None):
                return None
            helper(root.left, lis)
            lis.append(root.val)
            helper(root.right, lis)
        helper(root, lis)
        return lis
            