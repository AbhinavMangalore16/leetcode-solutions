# Last updated: 9/5/2026, 11:30:22 PM
1class Solution:
2    def firstStableIndex(self, nums: list[int], k: int) -> int:
3        n = len(nums)
4
5        resid = 0           
6        gMax = float('-inf')       
7        resMax = float('-inf') 
8
9        for i in range(n):
10            gMax = max(gMax, nums[i])
11            if i == resid:
12                resMax = max(resMax, nums[i])
13            if nums[i] < resMax - k:
14                resid = i + 1
15                resMax = gMax
16        return resid if resid < n else -1