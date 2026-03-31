# Last updated: 3/31/2026, 9:29:41 PM
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        s = set(nums)
        if nums[0]+nums[1]<=nums[2]:
            return "none"
        if len(s)==1:
            return "equilateral"
        elif len(s)==2:
            return "isosceles"
        else:
            return "scalene"