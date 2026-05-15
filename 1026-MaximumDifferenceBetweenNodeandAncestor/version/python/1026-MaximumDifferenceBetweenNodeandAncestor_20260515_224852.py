# Last updated: 5/15/2026, 10:48:52 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
9        def dfs(node, low, high):
10            if not node:
11                return (high-low)
12            low = min(low, node.val)
13            high = max(high, node.val)
14            ltree = dfs(node.left, low, high)
15            rtree = dfs(node.right, low, high)
16            return max(ltree, rtree)
17        return dfs(root, root.val, root.val)