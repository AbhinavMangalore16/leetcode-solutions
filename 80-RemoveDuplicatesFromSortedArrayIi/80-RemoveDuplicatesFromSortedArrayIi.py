# Last updated: 3/31/2026, 9:40:15 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        ptr = 2 
        for i in range(2,len(nums)):
            if nums[i] != nums[ptr-1] or nums[i] != nums[ptr-2]:
                nums[ptr] = nums[i]
                ptr +=1
        return len(nums[:ptr])

            