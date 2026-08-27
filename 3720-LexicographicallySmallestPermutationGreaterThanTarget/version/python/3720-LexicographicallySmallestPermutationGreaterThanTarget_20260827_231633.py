# Last updated: 8/27/2026, 11:16:33 PM
1class Solution:
2    def lexGreaterPermutation(self, s: str, target: str) -> str:
3        from collections import Counter
4        freq = Counter(s)
5        best_i = -1
6        for i, char in enumerate(target):
7            for c in "abcdefghijklmnopqrstuvwxyz":
8                if c > char and freq[c] > 0:
9                    best_i = i
10                    break 
11            if freq[char] > 0:
12                freq[char] -= 1
13            else:
14                break
15                
16        if best_i == -1:
17            return ""
18        freq = Counter(s)
19        res = []
20        for j in range(best_i):
21            res.append(target[j])
22            freq[target[j]] -= 1
23        for c in "abcdefghijklmnopqrstuvwxyz":
24            if c > target[best_i] and freq[c] > 0:
25                res.append(c)
26                freq[c] -= 1
27                break
28        for c in "abcdefghijklmnopqrstuvwxyz":
29            while freq[c] > 0:
30                res.append(c)
31                freq[c] -= 1
32                
33        return "".join(res)