# Last updated: 3/31/2026, 9:40:24 PM
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        c = 0
        ai = len(a) -1
        bi = len(b) -1
        while (ai>=0) or (bi>=0) or (c==1):
            if ai>=0:
                c+=int(a[ai])
                ai-=1
            if bi>=0:
                c+=int(b[bi])
                bi-=1
            res = str(c%2) + res
            c = c//2
        return res
