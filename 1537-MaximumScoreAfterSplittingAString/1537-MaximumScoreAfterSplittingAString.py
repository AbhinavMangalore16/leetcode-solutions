# Last updated: 3/31/2026, 9:34:32 PM
class Solution:
    def maxScore(self, s: str) -> int:
        zeros = s.count('0')
        res = -1
        z = 0
        n = len(s)
        for i in range(1, n):
            if s[i-1] == '0':
                z+=1
                zeros -=1 
            put = z+(n-zeros-i)
            res = max(res, put)
        return res