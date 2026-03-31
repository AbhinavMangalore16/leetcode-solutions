# Last updated: 3/31/2026, 9:33:42 PM
class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        corr = True
        rot_ch = 0
        for i in range(n):
            if nums[i]>nums[(i+1)%n]:
                rot_ch +=1
            if rot_ch>1:
                corr = False
                break
        return corr