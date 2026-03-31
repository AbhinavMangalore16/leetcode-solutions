# Last updated: 3/31/2026, 9:35:45 PM
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(h!=s for h, s in zip(heights, sorted(heights)))