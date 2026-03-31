# Last updated: 3/31/2026, 9:36:59 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        l = []
        def helper(root: 'Node'):
            if not root:
                return None
            for i in root.children:
                helper(i)
            l.append(root.val)
        helper(root)
        return l