# Last updated: 3/31/2026, 9:29:49 PM
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        maxx = -1
        p = 0
        for i in range(len(nums)):
            if nums[i]<p:
                maxx = nums[i] + p
            p+=nums[i]
        return maxx
        