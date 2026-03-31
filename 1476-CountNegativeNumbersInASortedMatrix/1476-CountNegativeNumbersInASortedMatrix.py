# Last updated: 3/31/2026, 9:34:47 PM
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        i,j=r-1,0
        ct = 0
        while i>-1 and j<c:
            if grid[i][j]<0:
                ct+=(c-j)
                i-=1
            else:
                j+=1
        return ct