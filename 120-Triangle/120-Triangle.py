# Last updated: 3/31/2026, 9:39:51 PM
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if n == 1:
            return triangle[0][0]
        dp = [[0]*(i) for i in range(1, n+1)]
        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            for j in range(i+1):
                if j==0:
                    dp[i][0] = dp[i-1][0] + triangle[i][0]
                elif j==i:
                    dp[i][i] = dp[i-1][i-1] + triangle[i][i]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        return min(dp[-1])