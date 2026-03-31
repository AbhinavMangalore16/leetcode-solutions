# Last updated: 3/31/2026, 9:30:56 PM
class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + 4 * n * (n-1) // 2