# Last updated: 3/31/2026, 9:37:07 PM
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = deque()
        ways = [[0,1],[1,0],[0,-1],[-1,0]]
        m = len(image)
        n = len(image[0])
        scolor = image[sr][sc]
        if scolor == color:
            return image
        queue.append([sr,sc])
        while queue:
            x, y = queue.popleft()
            image[x][y] = color
            for R, C in ways:
                row, col = x+R, y+C
                if (0 <= row < m and 0 <= col < n and image[row][col]==scolor):
                    image[row][col] = color
                    queue.append([row,col])
        return image
    