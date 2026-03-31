# Last updated: 3/31/2026, 9:30:57 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sums = []
        def dfs(root, lvl):
            if not root:
                return 
            if len(sums) == lvl:
                sums.append(0)
            sums[lvl]+=root.val 
            dfs(root.left, lvl+1)
            dfs(root.right, lvl+1)
        dfs(root, 0)
        if len(sums)<k:
            return -1
        return sorted(sums)[-k]