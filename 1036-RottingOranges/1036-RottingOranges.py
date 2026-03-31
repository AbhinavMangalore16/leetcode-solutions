# Last updated: 3/31/2026, 9:35:56 PM
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        R, C = len(grid), len(grid[0])
        dirn = [(0,1), (0,-1), (1,0), (-1,0)]
        fresh = 0
        queue = deque()
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
                elif grid[i][j] == 1:
                    fresh +=1 
        T = 0
        while queue: 
            x, y, t = queue.popleft()
            T = max(T, t)
            for dx, dy in dirn:
                row, col = x+dx, y+dy
                if (0<= row < R) and (0<=col<C) and grid[row][col] ==1:
                    grid[row][col] = 2
                    fresh -=1
                    queue.append((row, col, t+1))
        if fresh:
            return -1
        return T 