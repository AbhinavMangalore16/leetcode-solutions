# Last updated: 3/31/2026, 9:40:35 PM
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxx = 0
        for i in range(len(nums)):
            if i>maxx:
                return False
            maxx = max(maxx, i+nums[i])
        return True if maxx>=len(nums)-1 else False