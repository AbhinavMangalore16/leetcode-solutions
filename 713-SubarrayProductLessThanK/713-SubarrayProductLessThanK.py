# Last updated: 3/31/2026, 9:37:13 PM
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        count = 0
        pro = 1
        lp = 0
        for rp in range(len(nums)):
            pro = pro* nums[rp]
            while pro>=k:
                pro = pro//nums[lp]
                lp+=1
            count += (rp-lp) + 1
        return count 