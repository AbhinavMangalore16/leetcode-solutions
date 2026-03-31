# Last updated: 3/31/2026, 9:30:55 PM
class Solution:
    def helper(self, grid: List[List[int]], r: int, c: int, n:int, high: int):
        if (r<0) or (c<0) or (r>=n) or (c>=n) or grid[r][c]!=high:
            return False
        if grid[r][c]==(n*n-1):
            return True
        M1 = self.helper(grid, r-2, c+1, n, high+1)
        M2 = self.helper(grid, r-1, c+2, n, high+1)
        M3 = self.helper(grid, r+1, c+2, n, high+1)
        M4 = self.helper(grid, r+2, c+1, n, high+1)
        M5 = self.helper(grid, r+2, c-1, n, high+1)
        M6 = self.helper(grid, r+1, c-2, n, high+1)
        M7 = self.helper(grid, r-1, c-2, n, high+1)
        M8 = self.helper(grid, r-2, c-1, n, high+1)

        return M1 or M2 or M3 or M4 or M5 or M6 or M7 or M8

    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        return self.helper(grid, 0, 0, len(grid), 0)