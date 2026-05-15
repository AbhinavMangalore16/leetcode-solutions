# Last updated: 5/15/2026, 4:01:35 PM
1from functools import lru_cache
2class Solution:
3    def maxCoins(self, nums: List[int]) -> int:
4        nums = [1]+ nums+[1]
5        n = len(nums)
6        dp = [[0]*n for _ in range(n)]
7        for low in range(2,n):
8            for i in range(0,n-low):
9                j = i+low
10                for k in range(i+1, j):
11                    dp[i][j] = max(dp[i][j],
12                    dp[i][k]+dp[k][j]+nums[i]*nums[k]*nums[j])
13        return dp[0][n-1]