# Last updated: 3/31/2026, 9:37:58 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def helper(node: Optional[TreeNode], currSum:int)->int:
            if not node:
                return 0
            currSum += node.val
            numPaths = prefixSum[currSum-targetSum]
            prefixSum[currSum] += 1
            numPaths += helper(node.left, currSum)
            numPaths += helper(node.right, currSum)
            prefixSum[currSum] -=1
            return numPaths


        prefixSum = defaultdict(int)
        prefixSum[0] = 1
        return helper(root, 0)