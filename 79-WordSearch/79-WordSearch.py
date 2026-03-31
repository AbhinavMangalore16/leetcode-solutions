# Last updated: 3/31/2026, 9:40:16 PM
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def DFS(i,j,curr):
            if curr == len(word):
                return True
            if i<0 or i>=row or j<0 or j>=col or board[i][j] != word[curr]:
                return False
            cell = board[i][j]
            board[i][j] = 'visited'
            move = DFS(i,j+1,curr+1) or DFS(i+1,j,curr+1) or DFS(i-1,j,curr+1) or DFS(i,j-1,curr+1)
            board[i][j] = cell
            return move


        row,col = len(board), len(board[0])
        for i in range(row):
            for j in range(col):
                if DFS(i,j,curr=0):
                    return True
        return False       