# Last updated: 3/31/2026, 9:39:03 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def recur(root: Optional[TreeNode], ans: list, lvl: int):
            if not root:
                return 
            if lvl == len(ans):
                ans.append(root.val)
            recur(root.right, ans, lvl+1)
            recur(root.left, ans, lvl+1)
        ans = []
        recur(root, ans, 0)
        return ans