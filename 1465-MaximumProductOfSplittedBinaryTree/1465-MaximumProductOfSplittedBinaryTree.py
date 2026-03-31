# Last updated: 3/31/2026, 9:34:51 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def dfs_sum(node):
            if not node:
                return 0
            node.val+=dfs_sum(node.left)+dfs_sum(node.right)
            return node.val
        total = dfs_sum(root)
        Q = deque([root])
        maxx = -1
        while Q:
            node = Q.popleft()
            if not node:
                continue
            prod=node.val*(total-node.val)
            maxx = max(maxx, prod)
            if node.left:
                Q.append(node.left)
            if node.right:
                Q.append(node.right)
        return maxx % (10**9 +7)
            