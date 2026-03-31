# Last updated: 3/31/2026, 9:39:57 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root: Optional[TreeNode])->list:
            if not root:
                return [True, 0]
            leftbal = helper(root.left)
            rightbal = helper(root.right)
            cond = abs(leftbal[1]-rightbal[1]) <=1
            height = max(leftbal[1], rightbal[1])+1
            if leftbal[0] and rightbal[0] and cond:
                return [True, height]
            else:
                return [False, height]
        answer = helper(root)
        return answer[0]