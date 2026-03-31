# Last updated: 3/31/2026, 9:39:55 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def helper(node: Optional[TreeNode], currPath: List[int], currSum: int)->None:
            if not node:
                return 
            currPath.append(node.val)
            currSum += node.val
            if not node.left and not node.right and currSum==targetSum:
                paths.append(list(currPath))
            helper(node.left, currPath, currSum)
            helper(node.right, currPath, currSum)
            currPath.pop()

        paths = []
        helper(root, [], 0)
        return paths    