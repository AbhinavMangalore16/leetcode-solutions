# Last updated: 3/31/2026, 9:36:50 PM
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(dict)
        for s,d,w in flights: 
            graph[s][d] = w
        pri = [(0,src,k+1)]
        visited = [0]*n
        while pri:
            w,x,k = heapq.heappop(pri)
            if x == dst:
                return w
            if visited[x] >=k:
                continue
            visited[x] = k
            for y,dw in graph[x].items():
                heapq.heappush(pri,(w+dw, y, k-1))
        return -1
            