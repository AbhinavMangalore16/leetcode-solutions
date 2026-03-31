# Last updated: 3/31/2026, 9:40:29 PM
class Solution:
    def uniquePaths(self, rows: int, cols: int) -> int:
        dp = [[0]*(cols) for _ in range(rows)]
        for i in range(rows):
            dp[i][0] = 1
        for j in range(cols):
            dp[0][j] = 1
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[rows-1][cols-1]
        