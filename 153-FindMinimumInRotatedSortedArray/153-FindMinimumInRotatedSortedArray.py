# Last updated: 3/31/2026, 9:39:24 PM
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,h = 0, len(nums)-1
        while l<h:
            m = l+(h-l)//2
            if (nums[m-1]>nums[m]) and (nums[m+1]>nums[m]):
                return nums[m]
            elif (nums[m]>nums[h]):
                l = m+1
            else:
                h = m-1
        return nums[l]