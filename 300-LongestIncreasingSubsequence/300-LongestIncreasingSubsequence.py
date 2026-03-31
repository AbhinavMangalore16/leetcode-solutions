# Last updated: 3/31/2026, 9:38:18 PM
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1  

        lis = [nums[0]]
        for x in nums[1:]:
            if x > lis[-1]:
                lis.append(x)
            else:
                index = bisect.bisect_left(lis, x)
                lis[index] = x

        return len(lis)        