# Last updated: 9/11/2026, 3:53:38 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def averageOfSubtree(self, root: TreeNode) -> int:
9        self.C = 0
10        def help(node):
11            if node is None:
12                return (0, 0)
13            lS, lC = help(node.left)
14            rS, rC = help(node.right)
15            subS = lS+rS+node.val
16            subC = lC+rC+1
17            av = subS//subC
18            if av == node.val:
19                self.C+=1
20            return (subS, subC)
21        help(root)
22        return self.C