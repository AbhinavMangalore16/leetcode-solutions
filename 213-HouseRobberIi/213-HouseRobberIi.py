# Last updated: 3/31/2026, 9:38:54 PM
class Solution:
    def rob(self, nums: List[int]) -> int:
        r1,r2 = 0,0
        h1,h2 = 0,0
        for i in nums[1:]:
            robb = max(i+h1,h2)
            h1 = h2
            h2 = robb
        r1 = h2
        h1,h2 = 0,0
        for i in nums[:-1]:
            robb = max(i+h1,h2)
            h1 = h2
            h2 = robb
        r2 = h2
        return max(nums[0],r1,r2)