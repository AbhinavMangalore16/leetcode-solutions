# Last updated: 3/31/2026, 9:33:46 PM
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxs, mins = float('-inf'), float('inf')
        cur, curr = 0, 0
        for num in nums:
            cur += num
            curr += num
            maxs = max(cur, maxs)
            mins = min(curr, mins)
            if cur < 0:
                cur = 0
            if curr > 0:
                curr = 0
        return max(abs(mins), maxs)