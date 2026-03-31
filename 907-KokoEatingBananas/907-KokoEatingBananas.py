# Last updated: 3/31/2026, 9:36:28 PM
class Solution:
    def minEatingSpeed(self, piles: List[int], T: int) -> int:
        l, h = 1, max(piles)
        maxbanana = h
        while l<=h:
            mid = (h+l)//2
            tt = 0
            for i in range(len(piles)):
                tt += math.ceil(piles[i]/mid)
            if tt<=T:
                maxbanana = mid
                h = mid-1
            else:
                l = mid+1
        return maxbanana

