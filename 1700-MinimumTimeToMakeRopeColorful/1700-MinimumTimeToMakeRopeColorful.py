# Last updated: 3/31/2026, 9:34:02 PM
class Solution:
    def minCost(self, colors: str, needed: List[int]) -> int:
        total = 0
        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                total += min(needed[i], needed[i-1])
                needed[i] = max(needed[i], needed[i - 1])
        return total