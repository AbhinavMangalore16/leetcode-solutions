# Last updated: 3/31/2026, 9:37:27 PM
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}
        t = 0
        for i in range(len(tasks)):
            d[tasks[i]] = d.get(tasks[i], 0) +1
        mh = []
        for i in d.values():
            mh.append(-i)
        heapq.heapify(mh)
        qu = deque()
        while mh or qu:
            t = t+1
            if mh:
                tk = heapq.heappop(mh) +1
                if tk<0:
                    qu.append([tk , t+n])
            if qu and qu[0][1]<=t:
                heapq.heappush(mh, (qu.popleft()[0]))
        return t