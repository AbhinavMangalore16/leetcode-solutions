# Last updated: 3/31/2026, 9:40:27 PM
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dp = [[0]*(cols) for _ in range(rows)]
        for i in range(rows):
            if obstacleGrid[i][0]:
                break
            dp[i][0] = 1
        for j in range(cols):
            if obstacleGrid[0][j]:
                break
            dp[0][j] = 1
        for i in range(1,rows):
            for j in range(1,cols):
                dp[i][j] = 0 if obstacleGrid[i][j] else (dp[i-1][j]+dp[i][j-1])
        return dp[rows-1][cols-1]