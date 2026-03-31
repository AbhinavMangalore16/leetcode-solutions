# Last updated: 3/31/2026, 9:39:29 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lis = [] 
        def helper(root: Optional[TreeNode], lis: List[int]):
            if root is None:
                return None
            helper(root.left, lis)
            helper(root.right, lis)
            lis.append(root.val)
        helper(root, lis)
        return lis