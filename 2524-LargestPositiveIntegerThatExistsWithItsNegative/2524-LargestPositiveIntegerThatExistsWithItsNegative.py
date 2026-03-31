# Last updated: 3/31/2026, 9:31:30 PM
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        l,r = 0,len(nums)-1
        while(l<r):
            if (not nums[l]+nums[r]):
                return nums[r]
            elif (nums[l]+nums[r] < 0):
                l+=1
            else:
                r-=1
        return -1