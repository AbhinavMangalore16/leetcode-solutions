# Last updated: 3/31/2026, 9:39:15 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ct = 0
        el = nums[0]
        for i in range(len(nums)):
            if not ct:
                el = nums[i]
            if nums[i]==el:
                ct +=1
            else:
                ct -=1
        return el
            