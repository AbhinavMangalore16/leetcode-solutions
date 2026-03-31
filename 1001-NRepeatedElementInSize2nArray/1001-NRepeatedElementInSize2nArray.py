# Last updated: 3/31/2026, 9:36:04 PM
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)
        edge = nums[-1]
        for i in range(n-2):
            if nums[i] == nums[i+1] or nums[i]==nums[i+2]:
                edge = nums[i]
                break
        return edge