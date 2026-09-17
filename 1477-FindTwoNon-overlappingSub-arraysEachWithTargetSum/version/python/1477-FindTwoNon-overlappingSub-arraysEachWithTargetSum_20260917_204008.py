# Last updated: 9/17/2026, 8:40:08 PM
1class Solution:
2    def minSumOfLengths(self, arr: list[int], target: int) -> int:
3        pos = {0: -1}
4        n = len(arr)
5        s = 0
6        ans = n + 1
7        min_l = n
8        for i, x in enumerate(arr):
9            s += x
10            if s - target in pos:
11                j = pos[s - target]
12                length = i - j
13                ans = min(ans, length + (n if j == -1 else arr[j]))
14                min_l = min(min_l, length)
15            arr[i] = min_l
16            pos[s] = i
17        return -1 if ans == n + 1 else ans