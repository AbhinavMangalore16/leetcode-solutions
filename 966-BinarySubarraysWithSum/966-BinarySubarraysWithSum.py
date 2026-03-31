# Last updated: 3/31/2026, 9:36:12 PM
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        c = 0
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1]+num)
        d = {}
        for s in prefix:
            c += d.get(s-goal, 0) 
            d[s] = d.get(s,0)+ 1
        return c