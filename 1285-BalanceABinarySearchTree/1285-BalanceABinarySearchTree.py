# Last updated: 3/31/2026, 9:35:26 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            nodes.append(root)
            inorder(root.right)
        def balancer(lx, rx):
            if lx>rx: 
                return None
            mid = (lx+rx)//2
            l = balancer(lx, mid-1)
            r = balancer(mid+1, rx)
            nodes[mid].left = l
            nodes[mid].right = r
            return nodes[mid]
        inorder(root)
        return balancer(0, len(nodes)-1)