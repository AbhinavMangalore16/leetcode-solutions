# Last updated: 3/31/2026, 9:41:02 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uni = 0
        uniq_el = nums[0]
        for i in range(1,len(nums)):
            if nums[i] != uniq_el:
                uni+=1
                nums[uni] = nums[i]
                uniq_el = nums[uni]
        return uni+1


        return nums