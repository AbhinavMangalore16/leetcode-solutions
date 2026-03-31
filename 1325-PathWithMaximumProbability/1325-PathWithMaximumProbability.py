# Last updated: 3/31/2026, 9:35:18 PM
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        d = [0]*n
        d[start_node] = 1
        for i in range(n-1):
            f = False
            for j, (a,b) in enumerate(edges):
                if d[a]*succProb[j] > d[b]:
                    d[b] = d[a]*succProb[j]
                    f = True
                if d[b]*succProb[j] > d[a]:
                    d[a] = d[b] * succProb[j]
                    f = True
            if not f:
                break
        return d[end_node]