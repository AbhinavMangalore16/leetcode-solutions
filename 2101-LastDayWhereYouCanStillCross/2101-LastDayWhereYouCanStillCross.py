# Last updated: 3/31/2026, 9:33:09 PM
class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x: int, y: int) -> None:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        self.size[rx] += self.size[ry]

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        TOP = row * col
        BOTTOM = row * col + 1
        dsu = DSU(row * col + 2)
        grid = [[0] * col for _ in range(row)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def idx(r: int, c: int) -> int:
            return r * col + c
        for day in range(len(cells) - 1, -1, -1):
            r, c = cells[day][0] - 1, cells[day][1] - 1
            grid[r][c] = 1
            node = idx(r, c)
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc]:
                    dsu.union(node, idx(nr, nc))
            if r == 0:
                dsu.union(node, TOP)
            if r == row - 1:
                dsu.union(node, BOTTOM)
            if dsu.find(TOP) == dsu.find(BOTTOM):
                return day
        return 0