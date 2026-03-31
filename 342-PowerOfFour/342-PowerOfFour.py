# Last updated: 3/31/2026, 9:38:16 PM
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return (n>0) and (math.log2(n) % 2 == 0)