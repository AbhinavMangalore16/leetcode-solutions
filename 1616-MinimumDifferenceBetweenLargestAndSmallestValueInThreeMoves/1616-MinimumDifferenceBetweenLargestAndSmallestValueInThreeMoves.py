# Last updated: 3/31/2026, 9:34:21 PM
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums)<5:
            return 0
        nums.sort()
        diff = float("inf")
        for i in range(4):
            j = len(nums)-4+i
            diff = min(diff, nums[j] - nums[i])
        return diff