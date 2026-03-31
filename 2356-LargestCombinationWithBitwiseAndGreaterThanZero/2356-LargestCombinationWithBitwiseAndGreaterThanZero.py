# Last updated: 3/31/2026, 9:32:05 PM
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        res = 0
        for i in range(32):
            c = sum(1 for c in candidates if c & (1<<i))
            res = max(res, c)
        return res