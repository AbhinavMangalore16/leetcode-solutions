# Last updated: 3/31/2026, 9:37:24 PM
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(c**0.5)
        while(l<=r):
            ss = l**2 + r**2
            if ss == c:
                return True
            elif ss<c:
                l+=1
            else:
                r-=1
        return False