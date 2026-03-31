# Last updated: 3/31/2026, 9:36:56 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode(val)
        if not root:
            root = node
            return root
        par = root
        while 1:
            if val>=par.val:
                if par.right == None:
                    par.right = node
                    break
                else:
                    par = par.right
            else:
                if par.left == None:
                    par.left = node
                    break
                else:
                    par = par.left
        return root