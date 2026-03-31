# Last updated: 3/31/2026, 9:29:07 PM
class Solution:
    def maxOperations(self, s: str) -> int:
        res = 0
        c = 0
        z = True
        for ch in s:
            if ch == "1":
                c += 1
                z = True
            elif z == True:
                z = False
                res += c
        return res