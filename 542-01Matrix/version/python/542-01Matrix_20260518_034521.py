# Last updated: 5/18/2026, 3:45:21 AM
1class Solution:
2    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
3        
4        m,n = len(mat), len(mat[0])
5        dq = deque()
6        MX = m*n
7        for i in range(m):
8            for j in range(n):
9                if not mat[i][j]:
10                    dq.append((i,j))
11                else:
12                    mat[i][j]=MX
13        dirns = [(1,0), (-1,0), (0,1), (0,-1)]
14        while dq:
15            row,col =dq.popleft()
16            for dr,dc in dirns:
17                nr,nc = row+dr, col+dc
18                if 0<=nr<m and 0<=nc<n and mat[nr][nc]>mat[row][col]+1:
19                    dq.append((nr,nc))
20                    mat[nr][nc] = mat[row][col]+1
21        return mat
22
23
24