# Last updated: 3/31/2026, 9:33:28 PM
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0

        for i in range(len(nums) // 2):
            res = max(res, nums[i] + nums[-1 - i])

        return res