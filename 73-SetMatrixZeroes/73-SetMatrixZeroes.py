# Last updated: 3/31/2026, 9:40:20 PM
class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        m = len(mat)
        n = len(mat[0])
        c0 = 1
        for i in range(m):
            for j in range(n):
                if not mat[i][j]:
                    if j==0:
                        c0 = 0
                    else:
                        mat[i][0] = 0
                        mat[0][j] = 0
        for i in range(1,m):
            for j in range(1,n):
                if (not mat[i][0]) or (not mat[0][j]):
                    mat[i][j] = 0 
        if not mat[0][0]:
            for i in range(n):
                mat[0][i] = 0
        if not c0:
            for j in range(m):
                mat[j][0] = 0
        return None