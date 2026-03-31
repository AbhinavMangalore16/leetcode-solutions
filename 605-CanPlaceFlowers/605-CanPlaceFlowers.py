# Last updated: 3/31/2026, 9:37:29 PM
class Solution:
    def canPlaceFlowers(self, f: List[int], n: int) -> bool:
        l = len(f)
        for i in range(l):
            if not n:
                return True
            if not f[i] and (i==0 or not f[i-1]) and (i==(l-1) or not f[i+1]):
                f[i] = 1
                n-=1
        return not n