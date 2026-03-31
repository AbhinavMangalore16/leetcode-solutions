# Last updated: 3/31/2026, 9:29:35 PM
class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        res = ""
        for c in s:
            lev = min(ord(c)-ord('a'),ord('z')-ord(c)+1)
            if k>=lev:
                k-=lev
                res = res + ('a' if lev<=ord(c)-ord('a') else 'z')
            else:
                res = res + chr(ord(c)-k)
                k-=k
        return res