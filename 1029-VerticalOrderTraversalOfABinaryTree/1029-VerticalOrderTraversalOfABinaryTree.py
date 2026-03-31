# Last updated: 3/31/2026, 9:35:59 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        vertical_order = defaultdict(lambda: defaultdict(list))
        queue = deque([(root, 0, 0)])  # Use deque for efficient pop from the front
        
        while queue:
            node, h_d, lvl = queue.popleft()
            vertical_order[h_d][lvl].append(node.val)
            
            if node.left:
                queue.append((node.left, h_d - 1, lvl + 1))
            if node.right:
                queue.append((node.right, h_d + 1, lvl + 1))
        
        for h_d in sorted(vertical_order.keys()):
            column = []
            for lvl in sorted(vertical_order[h_d].keys()):
                column.extend(sorted(vertical_order[h_d][lvl]))
            res.append(column)
        
        return res