# Last updated: 3/31/2026, 9:40:46 PM
class Solution:
    def jump(self, nums: List[int]) -> int:
        j = 0
        bound = 0
        maxx = 0
        for i in range(len(nums)-1):
            maxx = max(maxx, i+nums[i])
            if i == bound:
                j+=1
                bound = maxx
        return j