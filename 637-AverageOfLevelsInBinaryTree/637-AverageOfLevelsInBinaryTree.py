# Last updated: 3/31/2026, 9:37:22 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        averages = []
        if not root:
            return averages
        queue = deque([root])
        while queue:
            lvl = len(queue)
            add = 0.0
            for i in range(lvl):
                node = queue.popleft()
                add += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            averages.append(add/lvl)
        return averages