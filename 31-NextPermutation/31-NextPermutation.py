# Last updated: 3/31/2026, 9:40:58 PM
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pt = -1
        for i in range(len(nums)-2 ,-1,-1):
            if nums[i] < nums[i+1]:
                pt = i
                break
        if pt==-1:
            nums.reverse()
        else:
            for j in range(len(nums)-1, pt,-1):
                if nums[j]>nums[pt]:
                    nums[j], nums[pt] = nums[pt], nums[j]
                    break
            nums[pt+1:] = reversed(nums[pt+1:])
        