# Last updated: 3/31/2026, 9:40:37 PM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx = -10000
        curr = 0
        for i in range(len(nums)):
            curr = curr + nums[i]
            if (maxx<curr):
                maxx = curr
            if (curr<0):
                curr = 0 
        return maxx