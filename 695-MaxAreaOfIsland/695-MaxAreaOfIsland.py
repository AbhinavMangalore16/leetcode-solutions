# Last updated: 3/31/2026, 9:37:15 PM
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        d = [(-1,0), (1,0), (0,1), (0,-1)]
        max_area = 0 
        def dfs(r,c):
            if r<0 or c<0 or r>=R or c>=C or (not grid[r][c]):
                return 0
            grid[r][c] = 0
            area = 1
            for dn in d:
                area += dfs(r+dn[0], c+dn[1])
            return area
        
        for r in range(R):
            for c in range(C):
                if grid[r][c]:
                    max_area = max(max_area, dfs(r,c))
        return max_area

        