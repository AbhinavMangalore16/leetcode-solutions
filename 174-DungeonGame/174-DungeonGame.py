# Last updated: 3/31/2026, 9:39:14 PM
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows = len(dungeon)
        cols = len(dungeon[0])
        dp=[[float('inf')]*(cols+1) for i in range(rows+1)]
        dp[rows][cols-1] = dp[rows-1][cols] = 1
        for i in range(rows-1, -1,-1):
            for j in range(cols-1, -1,-1):
                points = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
                dp[i][j] = max(1, points)
        return dp[0][0]
