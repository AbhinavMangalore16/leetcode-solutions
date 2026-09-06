# Last updated: 9/6/2026, 8:44:40 PM
1class Solution:
2    def numDistinct(self, s: str, t: str) -> int:
3        m,n = len(s), len(t)
4        dp=[0]*(n+1)
5        dp[0]=1
6        for i in range(1,m+1):
7            for j in range(n,0,-1):
8                if s[i-1] == t[j-1]:
9                    dp[j] = dp[j] + dp[j-1]
10        return dp[n]