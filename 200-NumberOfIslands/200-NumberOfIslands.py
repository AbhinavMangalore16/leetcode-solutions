# Last updated: 3/31/2026, 9:39:00 PM
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        dirn = [(0,1), (0,-1), (1,0),(-1,0)]
        visited = set()
        islands = 0

        def search(i,j):
            queue = deque()
            visited.add((i,j))
            queue.append((i,j))
            while queue:
                x, y = queue.popleft()
                for r, c in dirn:
                    row, col = x+r, y+c
                    if (0<=row<R) and (0<=col<C) and grid[row][col] == "1" and ((row, col) not in visited):
                        queue.append((row, col))
                        visited.add((row, col)) 

        for i in range(R):
            for j in range(C):
                if grid[i][j] == "1" and (i,j) not in visited:
                    search(i,j)
                    islands+=1
        return islands