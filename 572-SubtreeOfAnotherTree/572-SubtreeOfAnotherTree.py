# Last updated: 3/31/2026, 9:37:32 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.MOD = 10**9 + 7  # A large prime for modulo operation
    
    def computeHash(self, node):
        if not node:
            return 0  # Return 0 for null nodes (considered as base case)
        
        leftHash = self.computeHash(node.left)
        rightHash = self.computeHash(node.right)
        
        # Compute a combined hash using node value and its children hashes
        nodeHash = (leftHash * 31 + node.val * 7 + rightHash * 13) % self.MOD
        
        # Store hash to avoid recomputation and for matching subtrees
        node.hash = nodeHash
        return nodeHash
    
    def isSame(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root.hash != subRoot.hash:
            return False
        return self.isSame(root.left, subRoot.left) and self.isSame(root.right, subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        
        self.computeHash(root)
        self.computeHash(subRoot)
        
        if self.isSame(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    