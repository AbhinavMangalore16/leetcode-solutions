# Last updated: 3/31/2026, 9:40:18 PM
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,m,h = 0, 0, len(nums)-1
        while m<=h:
            if not nums[m]:
                nums[l], nums[m] = nums[m], nums[l]
                l+=1
                m+=1
            elif nums[m]==1:
                m+=1
            else:
                nums[m], nums[h] = nums[h], nums[m]
                h-=1
        
        