# Last updated: 3/31/2026, 9:40:03 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        L = []
        if not root:
            return L
        Q = deque([root])
        while Q: 
            lvl = []
            for i in range(len(Q)):
                node = Q.popleft()
                lvl.append(node.val)
                if node.left: 
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
            L.append(lvl)
        return L