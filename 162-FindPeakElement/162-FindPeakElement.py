# Last updated: 3/31/2026, 9:39:19 PM
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, h = 0, len(nums)-1
        while l<h:
            m = l + (h-l)//2
            if nums[m]>nums[m+1]:
                h = m
            else:
                l = m+1
        return h