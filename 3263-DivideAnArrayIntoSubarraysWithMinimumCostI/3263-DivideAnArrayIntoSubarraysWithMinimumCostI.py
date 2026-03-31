# Last updated: 3/31/2026, 9:29:48 PM
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        lis = sorted(nums[1:])
        return nums[0]+lis[0]+lis[1]
        