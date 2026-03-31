# Last updated: 3/31/2026, 9:37:38 PM
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        while (low<high):
            mid = low + (high-low)//2
            if mid%2:
                mid-=1
            if nums[mid] == nums[mid+1]:
                low = mid+2
            else:
                high = mid
        return nums[low]