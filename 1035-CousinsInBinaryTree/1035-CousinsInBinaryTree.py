# Last updated: 3/31/2026, 9:35:57 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def BFS(root, x, y):
            queue = deque([(root, None)])
            while queue:
                arr = set()
                for i in range(len(queue)):
                    ch, par = queue.popleft()
                    if ch.val == x or ch.val ==y:
                        if par:
                            arr.add(par.val)
                    if ch.left:
                        queue.append((ch.left, ch))
                    if ch.right:
                        queue.append((ch.right, ch))
                if len(arr)==2:
                    return True
            return False
        return BFS(root,x,y)