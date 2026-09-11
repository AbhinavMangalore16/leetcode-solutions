# Last updated: 9/11/2026, 9:48:39 PM
1class Solution:
2    def totalNumbers(self, digits: List[int]) -> int:
3        freq = [0] * 10
4        for d in digits:
5            freq[d] += 1
6
7        count = 0
8
9        for h in range(1, 10):
10            if freq[h] == 0:
11                continue
12            freq[h] -= 1
13
14            for t in range(0, 10):
15                if freq[t] == 0:
16                    continue
17                freq[t] -= 1
18
19                for u in range(0, 9, 2):
20                    if freq[u] > 0:
21                        count += 1
22
23                freq[t] += 1
24
25            freq[h] += 1
26
27        return count