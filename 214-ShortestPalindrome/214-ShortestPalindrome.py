# Last updated: 3/31/2026, 9:38:52 PM
class Solution:
    def KMP(self, s: str) -> int:
        n = len(s)
        pi = [0]*n
        j = 0
        for i in range(1, n):
            while j>0 and s[i]!=s[j]:
                j = pi[j-1]
            if s[i] == s[j]:
                j+=1
            pi[i]= j
        return pi
        if not s:
            return s
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        new = s+"$"+rev
        pi = self.KMP(new)
        added = rev[:len(s) - pi[-1]]
        return added+s