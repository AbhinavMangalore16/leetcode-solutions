# Last updated: 3/31/2026, 9:33:21 PM
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])
        visited = set()

        def dfs(r,c):
            if (r<0 or c<0 or r== rows or c==cols or 
            not grid2[r][c] or (r,c) in visited):
                return True
            visited.add((r,c))
            wanna = True
            if grid1[r][c] == 0:
                wanna = False
            wanna = dfs(r-1,c) and wanna
            wanna = dfs(r+1,c) and wanna
            wanna = dfs(r,c-1) and wanna
            wanna = dfs(r,c+1) and wanna
            return wanna

        subisles = 0 
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] and (r,c) not in visited and dfs(r,c):
                    subisles+=1
        return subisles