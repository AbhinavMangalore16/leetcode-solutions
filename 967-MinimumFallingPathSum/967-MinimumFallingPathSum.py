# Last updated: 3/31/2026, 9:36:11 PM
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0]*(cols) for _ in range(rows)]
        for j in range(cols):
            dp[0][j] = matrix[0][j]
        for i in range(1, rows):
            for j in range(cols):
                if j ==0:
                    dp[i][j] = matrix[i][j] + min(dp[i-1][j], dp[i-1][j+1])
                elif j == cols-1:
                    dp[i][j] = matrix[i][j] + min(dp[i-1][j-1], dp[i-1][j])
                else:
                    dp[i][j] = matrix[i][j]+min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])
        return min(dp[-1])
