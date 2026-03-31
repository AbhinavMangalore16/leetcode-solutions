# Last updated: 3/31/2026, 9:37:45 PM
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx = 0
        curr = 0
        for i in range(len(nums)):
            if nums[i]:
                curr+=1
                maxx = max(curr, maxx)
            else:
                curr = 0
        return maxx