# Last updated: 3/31/2026, 9:33:20 PM
import math
class Solution:
    def countTriples(self, n: int) -> int:
        sq = 0
        for i in range(1,n):
            for j in range(i+1,n):
                c = i*i + j*j
                C = int(math.sqrt(c))
                if C*C==c and C<=n:
                    sq+=2
        return sq