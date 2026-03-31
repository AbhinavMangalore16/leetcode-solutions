# Last updated: 3/31/2026, 9:37:37 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(root:Optional[TreeNode])->list:
            if not root:
                return [0,0]
            left = helper(root.left)
            right = helper(root.right)

            dialeft = left[0]
            diaright = right[0]
            sumheight = left[1]+right[1]

            return [max(dialeft,diaright,sumheight), max(left[1], right[1])+1]
        result = helper(root)
        return result[0]