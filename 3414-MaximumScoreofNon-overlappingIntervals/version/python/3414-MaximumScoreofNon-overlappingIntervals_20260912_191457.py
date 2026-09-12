# Last updated: 9/12/2026, 7:14:57 PM
1class Solution:
2    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
3        n = len(intervals)
4        order = sorted(range(n), key=lambda i: intervals[i][1]) 
5        rights = [intervals[i][1] for i in order]
6
7        prev = [(0, [])] * (n + 1)
8        for _ in range(4):
9            cur = [(0, [])] * (n + 1)
10            for p in range(1, n + 1):
11                i = order[p - 1] 
12                l, r, w = intervals[i]
13                j = bisect_left(rights, l) 
14                score, ids = prev[j]
15                cur[p] = min((score - w, sorted(ids + [i])), cur[p - 1])
16            prev = cur
17        return prev[n][1]