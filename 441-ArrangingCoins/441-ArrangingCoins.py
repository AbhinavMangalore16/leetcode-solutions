# Last updated: 3/31/2026, 9:37:55 PM
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int(math.floor(math.sqrt(2*n + 0.25) - 0.5))