# Last updated: 3/31/2026, 9:33:33 PM
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        opns = 0
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                continue
            else:
                make = nums[i-1]+1
                opns+=(make-nums[i])
                nums[i] = make
        return opns