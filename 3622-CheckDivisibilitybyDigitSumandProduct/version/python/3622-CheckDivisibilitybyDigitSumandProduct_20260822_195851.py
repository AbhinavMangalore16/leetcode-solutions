# Last updated: 8/22/2026, 7:58:51 PM
1class Solution:
2    def checkDivisibility(self, n: int) -> bool:
3        num = n
4        dp = 1
5        ds = 0
6        while(num!=0):
7            rem = num%10
8            dp*=rem
9            ds+=rem
10            num//=10 
11        return not n%(dp+ds)