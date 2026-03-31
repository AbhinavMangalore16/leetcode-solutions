# Last updated: 3/31/2026, 9:38:21 PM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l= 0
        for r in range(n):
            if nums[r]:
                nums[l] = nums[r]
                l+=1
        while l<n:
            nums[l] = 0
            l+=1
