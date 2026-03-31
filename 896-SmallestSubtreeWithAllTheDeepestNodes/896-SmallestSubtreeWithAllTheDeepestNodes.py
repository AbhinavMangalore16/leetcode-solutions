# Last updated: 3/31/2026, 9:36:31 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return 0, None

            lh, a = dfs(node.left)
            rh, b = dfs(node.right)

            if lh > rh:
                return lh + 1, a

            elif rh > lh:
                return rh + 1, b

            else:
                return lh + 1, node

        return dfs(root)[1]
