# Last updated: 3/31/2026, 9:29:28 PM
class Solution:
    def scoreOfString(self, s: str) -> int:
        summ = 0
        for i in range(len(s)-1):
            summ+= abs(ord(s[i])-ord(s[i+1]))
        return summ