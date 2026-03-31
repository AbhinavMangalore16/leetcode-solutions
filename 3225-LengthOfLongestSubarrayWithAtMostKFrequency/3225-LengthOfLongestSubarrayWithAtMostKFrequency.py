# Last updated: 3/31/2026, 9:29:57 PM
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        d = {}
        l = 0 
        r = 0 
        maxx = 0
        for r in range(len(nums)):
            d[nums[r]] = d.get(nums[r],0)+1
            if d[nums[r]] >k:
                while nums[l]!= nums[r]:
                    d[nums[l]]-=1
                    l+=1
                d[nums[l]]-=1
                l+=1
            maxx = max(maxx,r-l+1)
        return maxx