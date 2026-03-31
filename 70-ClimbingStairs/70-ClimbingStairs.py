# Last updated: 3/31/2026, 9:40:23 PM
class Solution:
    def climbStairs(self, n: int) -> int:
        fir, sec = 1,1
        for i in range(n-1):
            stored = fir
            fir = fir+sec
            sec = stored
        return fir