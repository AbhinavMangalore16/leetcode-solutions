# Last updated: 5/15/2026, 3:58:11 PM
1from functools import lru_cache
2class Solution:
3    def maxCoins(self, nums: List[int]) -> int:
4        nums = [1]+ nums+[1]
5        N=len(nums)
6        @lru_cache(None)
7        def iter(l,h):
8            if h<=l+1:
9                return 0
10            maxx = 0
11            for k in range(l+1,h):
12                pres = nums[l]*nums[k]*nums[h]
13                total = iter(l,k)+iter(k,h)+pres
14                maxx = max(maxx, total)
15            return maxx
16        ans = iter(0, N-1)
17        return ans