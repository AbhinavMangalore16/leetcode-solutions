# Last updated: 3/31/2026, 9:28:52 PM
import heapq

class State:
    def __init__(self, x, y, distance):
        self.x = x
        self.y = y
        self.distance = distance

    def __lt__(self, other):
        return self.distance < other.distance


class Solution:
    def minTimeToReach(self, moveTime):
        n, m = len(moveTime), len(moveTime[0])
        INF = float('inf')
        
        distance = [[INF] * m for _ in range(n)]
        visited = [[False] * m for _ in range(n)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        distance[0][0] = 0
        priority_queue = []
        heapq.heappush(priority_queue, State(0, 0, 0))

        while priority_queue:
            current = heapq.heappop(priority_queue)

            if visited[current.x][current.y]:
                continue

            if current.x == n - 1 and current.y == m - 1:
                break

            visited[current.x][current.y] = True

            for dx, dy in directions:
                nx, ny = current.x + dx, current.y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    new_distance = max(distance[current.x][current.y], moveTime[nx][ny]) + (current.x + current.y) % 2 + 1
                    if new_distance < distance[nx][ny]:
                        distance[nx][ny] = new_distance
                        heapq.heappush(priority_queue, State(nx, ny, new_distance))

        return distance[n - 1][m - 1]
