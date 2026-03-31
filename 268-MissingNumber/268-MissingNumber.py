# Last updated: 3/31/2026, 9:38:26 PM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxx = len(nums)
        summ = 0
        for i in range(len(nums)):
            summ+=nums[i]
        miss = ((maxx*(maxx+1))//2) - summ
        return miss