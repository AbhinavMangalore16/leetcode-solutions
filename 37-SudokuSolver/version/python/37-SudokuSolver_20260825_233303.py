# Last updated: 8/25/2026, 11:33:03 PM
1class Solution:
2    def solveSudoku(self, board: list[list[str]]) -> None:
3        """
4        Do not return anything, modify board in-place instead.
5        """
6        rows = [set() for _ in range(9)]
7        cols = [set() for _ in range(9)]
8        boxes = [set() for _ in range(9)]
9        empty_cells = []
10        for r in range(9):
11            for c in range(9):
12                val = board[r][c]
13                if val == '.':
14                    empty_cells.append((r, c))
15                else:
16                    rows[r].add(val)
17                    cols[c].add(val)
18                    box_index = (r // 3) * 3 + c // 3 
19                    boxes[box_index].add(val)
20
21        def backtrack(index: int) -> bool:
22            if index == len(empty_cells):
23                return True
24            
25            r, c = empty_cells[index]
26            box_index = (r // 3) * 3 + c // 3
27            for num in range(1, 10):
28                val = str(num)
29                if val not in rows[r] and val not in cols[c] and val not in boxes[box_index]:
30                    board[r][c] = val
31                    rows[r].add(val)
32                    cols[c].add(val)
33                    boxes[box_index].add(val)
34                    if backtrack(index + 1):
35                        return True
36                    
37                    board[r][c] = '.'
38                    rows[r].remove(val)
39                    cols[c].remove(val)
40                    boxes[box_index].remove(val)
41                    
42            return False
43        backtrack(0)