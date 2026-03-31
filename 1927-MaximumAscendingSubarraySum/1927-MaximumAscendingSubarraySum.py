# Last updated: 3/31/2026, 9:33:34 PM
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr = ans = nums[0]
        for i in range(1, len(nums)):
            curr = curr + nums[i] if nums[i] > nums[i-1] else nums[i]
            ans = max(ans, curr)
        return ans