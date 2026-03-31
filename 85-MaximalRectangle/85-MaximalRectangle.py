# Last updated: 3/31/2026, 9:40:11 PM
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        res = 0
        cols = len(matrix[0])
        dp = [0] * cols

        for row in matrix:
            for i in range(cols):
                if row[i] == "1":
                    dp[i]+=1
                else:
                    dp[i] = 0   
            stk = []
            for j in range(cols+1):
                curr = dp[j] if j < cols else 0
                while stk and dp[stk[-1]] > curr:
                    h = dp[stk.pop()]
                    w = j if not stk else j-stk[-1]-1
                    res = max(res,h*w)
                stk.append(j)
        return res