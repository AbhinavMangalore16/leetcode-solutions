# Last updated: 3/31/2026, 9:31:16 PM
class Solution:
    def pivotInteger(self, n: int) -> int:
        piv = sqrt((n*(n+1))//2)
        if piv%1 == 0:
            return int(piv)
        else:
            return -1