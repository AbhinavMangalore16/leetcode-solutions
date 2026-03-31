# Last updated: 3/31/2026, 9:37:11 PM
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def helper(d):
            c = 0
            j = 0
            for i in range(len(nums)):
                while j<len(nums) and nums[j]-nums[i] <= d:
                    j+=1
                c += (j-i-1)
            return c

        nums.sort()
        l, h = 0, nums[-1]-nums[0]

        while l<h:
            m = (l+h)//2
            if helper(m)<k:
                l = m+1
            else:
                h = m
        return l

        