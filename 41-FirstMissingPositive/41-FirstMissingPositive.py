# Last updated: 3/31/2026, 9:40:49 PM
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [num for num in nums if num>0]
        if not nums:
            return 1
        nums.sort()
        if nums[0]!=1 or nums[-1]<=0:
            return 1
        for i in range(1, len(nums)):
            if (nums[i] - nums[i-1])>1:
                return nums[i-1]+1
        return nums[-1]+1 