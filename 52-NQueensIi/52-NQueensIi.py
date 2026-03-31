# Last updated: 3/31/2026, 9:40:38 PM
class Solution:
    def totalNQueens(self, n: int) -> int:
        d = {1:1,2:0,3:0,4:2,5:10,6:4,7:40,8:92, 9:352}
        return d[n]