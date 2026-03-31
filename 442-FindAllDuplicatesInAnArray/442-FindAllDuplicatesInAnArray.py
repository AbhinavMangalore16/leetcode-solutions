# Last updated: 3/31/2026, 9:37:57 PM
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dup = []
        for i in nums:
            if nums[abs(i)-1]<0:
                dup.append(abs(i))
            else:
                nums[abs(i)-1] *= -1
        return dup
        