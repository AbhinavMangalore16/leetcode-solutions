# Last updated: 3/31/2026, 9:29:33 PM
class UnionFind:
    def __init__(self, N):
        self.uni = list(range(N))
        self.n = [1]*N
    def find(self, el):
        if self.uni[el] !=el:
            self.uni[el] = self.find(self.uni[el])
        return self.uni[el]
    def union(self, el1, el2):
        uni1, uni2 = self.find(el1), self.find(el2)
        if uni1 == uni2:
            return False
        if self.n[uni1] > self.n[uni2]:
            self.uni[uni2] = uni1
            self.n[uni1] += self.n[uni2]
        else:
            self.uni[uni1] = uni2
            self.n[uni2] += self.n[uni1]
        return True

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        def lamb(ui,vi):
            if ui == vi:
                return 0
            e1, e2 = UF.find(ui), UF.find(vi)
            return gh[e1] if e1 == e2 else -1
        gh = [-1]*n
        UF = UnionFind(n)
        for u, v , ext in edges:
            UF.union(u,v)
        for u, _, w in edges:
            r = UF.find(u)
            gh[r] = gh[r]&w
        return [lamb(U,V) for U, V in query]