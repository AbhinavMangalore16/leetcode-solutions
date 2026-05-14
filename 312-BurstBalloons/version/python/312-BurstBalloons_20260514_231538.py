# Last updated: 5/14/2026, 11:15:38 PM
1class Solution:
2    def maxCoins(self, nums: List[int]) -> int:
3        nums = [1] + nums + [1]
4        n = len(nums)
5        dp = [[0]*n for _ in range(n)]
6        for ls in range(2,n):
7            for l in range(n-ls):
8                r = l+ls
9                for k in range(l+1, r):
10                    dp[l][r] = max(
11                        dp[l][r],
12                        dp[l][k]+dp[k][r]+nums[l]*nums[k]*nums[r]
13                    ) 
14        return dp[0][n-1]