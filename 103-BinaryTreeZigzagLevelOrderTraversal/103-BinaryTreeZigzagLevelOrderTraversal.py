# Last updated: 3/31/2026, 9:40:02 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        trav = []
        if not root:
            return trav
        queue = [root]
        ltr = True
        while queue:
            lvl = [None] * len(queue)
            for i in range(len(queue)):
                front = queue.pop(0)
                ind = i if ltr else len(lvl)-1-i
                lvl[ind] = front.val
                if (front.left):
                    queue.append(front.left)
                if (front.right):
                    queue.append(front.right)
            trav.append(lvl)
            ltr = not ltr
        return trav