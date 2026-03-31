# Last updated: 3/31/2026, 9:34:05 PM
class Solution:
    def maxDepth(self, s: str) -> int:
        maxdepth = 0
        depth = 0
        for i in s:
            if i == "(":
                depth +=1
                maxdepth = max(depth, maxdepth)
            elif i==")":
                depth-=1
        return maxdepth