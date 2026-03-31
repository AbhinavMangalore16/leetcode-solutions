# Last updated: 3/31/2026, 9:31:49 PM
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        bp = 0 
        hashing = {}
        for i in range(len(nums)):
            pos = i - nums[i]
            gpc = hashing.get(pos, 0)
            bpc = i-gpc
            bp+=bpc
            hashing[pos] = gpc +1
        return bp
