# Last updated: 3/31/2026, 9:29:04 PM
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def dijkstra(O: int, D: int, g: Dict[int, List[Tuple[int, int]]])-> int:
            heap = [(0, O)]
            dist = [float('inf')]*n
            dist[O] = 0
            while heap:
                currd, currn = heappop(heap)
                if currn == D:
                    return currd
                if currd> dist[currn]:
                    continue
                for neighbor, w in g[currn]:
                    ndist = currd+w
                    if ndist < dist[neighbor]:
                        dist[neighbor] = ndist
                        heappush(heap, (ndist, neighbor))
            return dist[D]
        g = {i: [] for i in range(n)}
        for i in range(n-1):
            g[i].append((i+1, 1))
        res = []
        for u, v in queries:
            g[u].append((v,1))
            minpath = dijkstra(0,n-1, g)
            res.append(minpath)
        return res