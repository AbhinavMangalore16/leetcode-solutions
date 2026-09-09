# Last updated: 9/10/2026, 2:03:04 AM
1class Solution:
2    def countCommas(self, n: int) -> int:
3        ct = 0
4        b = 999
5        T = 999
6        if n <= 999:
7            return 0
8        while T < n:
9            ct += n - T
10            T = T * 1000 + b
11        return ct