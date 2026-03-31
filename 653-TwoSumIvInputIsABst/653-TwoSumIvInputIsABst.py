# Last updated: 3/31/2026, 9:37:20 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        l = []
        def inorder(root: Optional[TreeNode])-> None:
            if not root:
                return 
            inorder(root.left)
            l.append(root.val)
            inorder(root.right)
        inorder(root)
        i, j = 0, len(l)-1
        while i<j:
            if k == l[i]+l[j]:
                return True
            elif k> l[i]+l[j]:
                i+=1
            else:
                j-=1
        return False