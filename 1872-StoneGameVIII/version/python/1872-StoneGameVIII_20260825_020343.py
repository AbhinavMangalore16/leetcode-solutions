# Last updated: 8/25/2026, 2:03:43 AM
1class Solution:
2    def stoneGameVIII(self, stones: List[int]) -> int:
3        def presum(stones,n):
4            pre = []
5            curr = 0
6            for i in range(n):
7                curr+=stones[i]
8                pre.append(curr)
9            return pre
10        n = len(stones)
11        pres = presum(stones,n)
12        dp = [0]*n
13        dp[n-1]=pres[n-1]
14        for i in range(n-2,0,-1):
15            dp[i] = max(dp[i+1], pres[i]-dp[i+1])
16        return dp[1]
17
18