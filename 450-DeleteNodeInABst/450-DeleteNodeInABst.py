# Last updated: 3/31/2026, 9:37:52 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key<root.val:
            root.left = self.deleteNode(root.left, key)
        elif key>root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                return None
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            root.val = self.inorderSucc(root.right)
            root.right = self.deleteNode(root.right, root.val)
        return root
    def inorderSucc(self, node:TreeNode)->int:
        while node.left:
            node = node.left
        return node.val