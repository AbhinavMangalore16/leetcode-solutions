# Last updated: 3/31/2026, 9:29:44 PM
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        pmax = cmin = cmax = pcnt = 0
        for v in nums:
            ccnt = v.bit_count()
            if pcnt == ccnt:
                cmin = min(cmin, v)
                cmax = max(cmax, v)
            elif cmin < pmax:
                return False
            else:
                pmax = cmax
                cmin = cmax = v
                pcnt = ccnt
        return cmin >= pmax