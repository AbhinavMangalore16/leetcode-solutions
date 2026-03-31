# Last updated: 3/31/2026, 9:38:43 PM
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0