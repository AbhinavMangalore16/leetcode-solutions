# Last updated: 9/7/2026, 6:34:50 PM
1class Solution:
2    def distinctSubseqII(self, s: str) -> int:
3        tot = 0
4        dp = [0] * 26
5        MOD = 10**9 + 7
6        for c in s:
7            c = ord(c) - 97
8            new = tot + 1 - dp[c]
9            tot = (tot + new) % MOD
10            dp[c] = (dp[c] + new) % MOD
11        return tot 